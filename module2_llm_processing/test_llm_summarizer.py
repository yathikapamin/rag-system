import os
import json
from llm_summarizer import process_pdf_reader_data

# Ensure API key is set or the test will fail
if not os.getenv("GEMINI_API_KEY"):
    print("Warning: GEMINI_API_KEY is not set in your environment variables.")
    print("You will need to set it to successfully run these tests.")
    print("Example (Windows): set GEMINI_API_KEY=your_key_here\n")

def run_tests():
    from PIL import Image, ImageDraw
    img = Image.new('RGB', (100, 30), color = (73, 109, 137))
    d = ImageDraw.Draw(img)
    d.text((10,10), "Test Image", fill=(255,255,0))
    img.save('mock_image.png')

    print("--- Testing LLM_Summarizer ---")
    
    # Test Case 1: Text Content
    print("\n[Test 1] Text Summarization")
    text_input = {
        "document_id": "doc_001",
        "page_number": 1,
        "content_type": "Text",
        "extracted_content": "Photosynthesis is a system of biological processes by which photosynthetic organisms, such as most plants, algae, and cyanobacteria, convert light energy, typically from sunlight, into the chemical energy necessary to fuel their metabolism.",
        "content_location": "Paragraph 1"
    }
    
    try:
        text_output = process_pdf_reader_data(text_input)
        print("Input Text:", text_input["extracted_content"])
        print("Generated Summary:", text_output["generated_summary"])
        print("Status:", text_output["processing_status"])
        print("Full Output JSON:\n", json.dumps(text_output, indent=2))
    except Exception as e:
        print("Error during Test 1:", e)

    # Test Case 2: Image Content (Requires a real image path to succeed fully)
    print("\n[Test 2] Image Summarization (Mock Path)")
    image_input = {
        "document_id": "doc_001",
        "page_number": 2,
        "content_type": "Image",
        "generated_image_path": "mock_image.png",
        "content_location": "Top right corner"
    }
    
    try:
        image_output = process_pdf_reader_data(image_input)
        print("Image Path:", image_input["generated_image_path"])
        print("Generated Summary:", image_output["generated_summary"])
        print("Status:", image_output["processing_status"])
        print("Full Output JSON:\n", json.dumps(image_output, indent=2))
    except Exception as e:
        print("Error during Test 2:", e)

if __name__ == "__main__":
    run_tests()
