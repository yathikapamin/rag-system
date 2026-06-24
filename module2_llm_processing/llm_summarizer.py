import os
import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
from PIL import Image

# Load environment variables from a .env file if present
load_dotenv()

# Defer Gemini client initialization to avoid import-time crash when API key is missing
client = None

class PDFReaderInput(BaseModel):
    page_number: int
    content_type: str  # "Text" or "Image"
    extracted_content: Optional[str] = None
    generated_image_path: Optional[str] = None
    content_location: Optional[str] = None
    document_id: Optional[str] = None

class LLMSummarizerOutput(BaseModel):
    document_id: Optional[str]
    page_number: int
    content_type: str
    original_extracted_content: Optional[str]
    generated_summary: str
    summary_length: int
    processing_status: str
    timestamp: str

class LLMSummarizerService:
    def summarize(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Takes input data from PDF_Reader, generates a summary using Gemini, 
        and returns the structured Output.
        """
        try:
            # Validate input data against schema
            input_data = PDFReaderInput(**data)
            
            summary = ""
            status = "Success"
            
            api_key = os.environ.get("GEMINI_API_KEY") or "AIzaSyDE_YmbW64AuIgUgiV45Fu0Xzmevb8fPSw"
            if not api_key or api_key.lower() == "mock":
                # Fallback to mock summary in absence of an API key
                if input_data.content_type.lower() == "text":
                    summary = f"[Mock Summary] This is a mock summary for page {input_data.page_number}."
                else:
                    summary = f"[Mock Image Description] This is a mock description for page {input_data.page_number}."
                status = "Success"
            else:
                global client
                if client is None:
                    client = genai.Client(api_key=api_key)
                
                import time
                retries = 3
                wait_seconds = 15
                
                if input_data.content_type.lower() == "text":
                    if not input_data.extracted_content:
                        raise ValueError("Content type is Text, but no extracted_content provided.")
                    
                    prompt = f"Please provide a concise summary of the following text:\n\n{input_data.extracted_content}"
                    
                    for attempt in range(retries):
                        try:
                            response = client.models.generate_content(
                                model='gemini-2.5-flash',
                                contents=prompt
                            )
                            summary = response.text
                            break
                        except Exception as e:
                            if "429" in str(e) and attempt < retries - 1:
                                print(f"[Module 2] Rate limited (429). Retrying in {wait_seconds}s (Attempt {attempt + 1}/{retries})...")
                                time.sleep(wait_seconds)
                                continue
                            raise
                    
                elif input_data.content_type.lower() == "image":
                    if not input_data.generated_image_path:
                        raise ValueError("Content type is Image, but no generated_image_path provided.")
                    
                    try:
                        img = Image.open(input_data.generated_image_path)
                        prompt = "Describe this image in detail and summarize any text or charts visible in it."
                        
                        for attempt in range(retries):
                            try:
                                response = client.models.generate_content(
                                    model='gemini-2.5-flash',
                                    contents=[prompt, img]
                                )
                                summary = response.text
                                break
                            except Exception as e:
                                if "429" in str(e) and attempt < retries - 1:
                                    print(f"[Module 2] Rate limited (429). Retrying in {wait_seconds}s (Attempt {attempt + 1}/{retries})...")
                                    time.sleep(wait_seconds)
                                    continue
                                raise
                    except Exception as e:
                        status = f"Failed to process image: {str(e)}"
                        summary = ""
                else:
                    status = f"Unknown content_type: {input_data.content_type}"
                
        except Exception as e:
            status = f"Error: {str(e)}"
            input_data = PDFReaderInput(**data) if 'input_data' not in locals() else input_data
            summary = ""

        # Prepare output
        timestamp = datetime.datetime.now().isoformat()
        
        output_data = LLMSummarizerOutput(
            document_id=input_data.document_id if 'input_data' in locals() else data.get("document_id"),
            page_number=input_data.page_number if 'input_data' in locals() else data.get("page_number", -1),
            content_type=input_data.content_type if 'input_data' in locals() else data.get("content_type", "Unknown"),
            original_extracted_content=input_data.extracted_content if 'input_data' in locals() else data.get("extracted_content"),
            generated_summary=summary,
            summary_length=len(summary),
            processing_status=status,
            timestamp=timestamp
        )
        
        return output_data.dict()

# Example usage function for easy testing
def process_pdf_reader_data(data: Dict[str, Any]) -> Dict[str, Any]:
    service = LLMSummarizerService()
    return service.summarize(data)
