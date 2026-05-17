from models.embedding_model import get_embedding

def generate_embedding(summary_text):

    embedding_vector = get_embedding(summary_text)

    return {
        "embedding_vector": embedding_vector,
        "embedding_dimension": len(embedding_vector)
    }