import os
import json

# Module Imports
from module1_pdf_extractor.extractor import extract_pdf
from module2_llm_processing.summarizer import process_module_data
from module3_embedding_generator.services.embedding_service import generate_embedding
from module4_vector_database.vector_storage import VectorDBStorage


def run_pipeline(pdf_path):

    print("Pipeline Started")

    # ---------------- MODULE 1 ----------------
    print("Running Module 1 - PDF Extraction")

    extracted_data = extract_pdf(pdf_path)

    print("Module 1 Completed\n")



    # Initialize Vector DB
    vector_db = VectorDBStorage(db_folder="vector_store")


    # Process each extracted page
    for page_data in extracted_data:

        # ---------------- MODULE 2 ----------------
        print("Running Module 2 - Summarization")

        summary_data = process_module_data(page_data)

        print("Module 2 Completed\n")


        # ---------------- MODULE 3 ----------------
        print("Running Module 3 - Embedding")

        embedding_data = generate_embedding(
            summary_data["generated_summary"]
        )

        print("Module 3 Completed\n")


        # ---------------- MODULE 4 ----------------
        print("Running Module 4 - Vector Storage")

        record = {
            "document_name": page_data.get("document_id"),
            "page_number": page_data.get("page_number"),
            "summary": summary_data.get("generated_summary"),
            "embedding": embedding_data.get("embedding_vector")
        }

        vector_db.store_records([record])

        print("Module 4 Completed\n")


    print("Pipeline Finished")


if __name__ == "__main__":
    run_pipeline("sample.pdf")
