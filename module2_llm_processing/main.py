from module1_extractor import MockPDFExtractor
from summarizer import process_module_data
import json

def run_project_pipeline():
    print("--- STARTING RAG PIPELINE ---")
    
    # 1. Your friend runs their Module 1
    extractor = MockPDFExtractor()
    extracted_data = extractor.extract_page("my_textbook.pdf", 1)
    
    print("\n--- DATA LEAVING MODULE 1 ---")
    print(json.dumps(extracted_data, indent=2))
    
    # 2. They pass that data directly into YOUR Module 2!
    print("\n[Module 2] Generating AI Summary...")
    final_output = process_module_data(extracted_data)
    
    # 3. Your module passes the result to the next person!
    print("\n--- DATA LEAVING MODULE 2 (Ready for Module 3) ---")
    print(json.dumps(final_output, indent=2))

if __name__ == "__main__":
    run_project_pipeline()
