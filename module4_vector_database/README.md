# Module 4 - Vector Database Storage

## Module Description
Module 4 stores embeddings, summaries, and metadata into a vector database for efficient retrieval in the Multimodal RAG system.

---

## Purpose
This module receives embeddings generated from Module 3 and stores them in a vector database along with metadata such as page number, summary, content type, and content location.

---

## Input Format

Input is received from Module 3 in JSON format.

Example:

```json
[
    {
        "document_name": "sample.pdf",
        "page_number": 1,
        "content_type": "text",
        "summary": "AI concepts",
        "embedding": [0.12, 0.45, 0.87],
        "metadata": {
            "location": "Page 1 Paragraph 2"
        }
    }
]
```

---

## Output Format

```json
{
    "status": "success",
    "stored_records": 2,
    "vector_db_path": "vector_store/faiss_index.bin",
    "metadata_path": "vector_store/metadata.pkl"
}
```

---

## Libraries Used

- FAISS
- NumPy
- Pickle
- OS
- Datetime

---

## Folder Structure

```txt
module_4/
│── main.py
│── vector_storage.py
│── sample_input.json
│── requirements.txt
│── README.md
│── vector_store/
```

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run Module 4

```bash
python main.py
```

---

## Output Files

After execution:

- `faiss_index.bin` → Stores vector embeddings
- `metadata.pkl` → Stores metadata

Both files are saved inside `vector_store/`
