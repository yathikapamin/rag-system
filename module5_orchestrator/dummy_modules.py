def extract_pdf(pdf_path):

    return {
        "document_name": pdf_path,
        "page": 1,
        "text": "AI improves healthcare",
        "images": ["page1.png"]
    }


def summarize(data):

    return {
        "summary": "AI helps healthcare using prediction systems."
    }


def generate_embedding(summary_data):

    return {
        "embedding": [0.12, 0.44, 0.91]
    }


def store_vector(data):

    return {
        "status": "Stored Successfully"
    }
