from pdf_reader import MockPDFExtractor
from llm_summarizer import process_pdf_reader_data
import json

def run_project_pipeline():
    print("--- STARTING RAG PIPELINE ---")
    
    # 1. Your friend runs their PDF_Reader
    extractor = MockPDFExtractor()
    extracted_data = extractor.extract_page("my_textbook.pdf", 1)
    
    print("\n--- DATA LEAVING PDF_READER ---")
    print(json.dumps(extracted_data, indent=2))
    
    # 2. They pass that data directly into YOUR LLM_Summarizer!
    print("\n[LLM_Summarizer] Generating AI Summary...")
    final_output = process_pdf_reader_data(extracted_data)
    
    # 3. Your module passes the result to the next person!
    print("\n--- DATA LEAVING LLM_SUMMARIZER (Ready for downstream tasks) ---")
    print(json.dumps(final_output, indent=2))

if __name__ == "__main__":
    run_project_pipeline()
