from dummy_modules import *

def run_pipeline(pdf_path):

    print("Pipeline Started")

    extracted_data = extract_pdf(pdf_path)
    print("Module 1 Completed")
    print(extracted_data)

    summary = summarize(extracted_data)
    print("Module 2 Completed")
    print(summary)

    embedding = generate_embedding(summary)
    print("Module 3 Completed")
    print(embedding)

    result = store_vector({
        "extraction": extracted_data,
    "summary": summary,
    "embedding": embedding
    })

    print("Module 4 Completed")
    print(result)

    print("Pipeline Finished")


run_pipeline("sample.pdf")