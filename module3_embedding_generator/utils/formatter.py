from config import EMBEDDING_MODEL
from utils.helpers import get_current_timestamp

def format_output(input_data, embedding_data):

    return {
        "document_id": input_data["document_id"],
        "page_number": input_data["page_number"],
        "content_type": input_data["content_type"],
        "generated_summary": input_data["generated_summary"],

        "embedding_model": EMBEDDING_MODEL,

        "embedding_dimension": embedding_data["embedding_dimension"],

        "embedding_vector": embedding_data["embedding_vector"],

        "metadata": {
            "summary_length": len(input_data["generated_summary"]),
            "timestamp": get_current_timestamp()
        },

        "processing_status": "success"
    }