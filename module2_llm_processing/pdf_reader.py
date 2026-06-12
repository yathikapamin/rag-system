class MockPDFExtractor:
    def extract_page(self, filepath: str, page_num: int):
        print(f"[PDF_Reader] Reading {filepath}, Page {page_num}...")
        # Imagine your friend's complex PDF extraction logic happens here!
        
        # They return their data as a dictionary:
        return {
            "document_id": "textbook_ch1",
            "page_number": page_num,
            "content_type": "Text",
            "extracted_content": "Artificial Intelligence (AI) is the intelligence of machines or software, as opposed to the intelligence of living beings, primarily of humans.",
            "content_location": "Paragraph 1"
        }
