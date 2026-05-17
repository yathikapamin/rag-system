# Module 3 - Embedding Generation Module
# 1. Module Description


## Purpose of the Module
The Embedding Generation Module is responsible for converting summarized text into vector embeddings for semantic search and retrieval in the RAG (Retrieval-Augmented Generation) system.

This module receives summarized content generated from Module 2 and transforms the textual information into numerical vector representations using embedding models.

These embeddings help the Vector Database retrieve semantically relevant information during user queries.

---

## What the Module Does
- Receives summarized text from Module 2
- Validates incoming data
- Cleans and preprocesses summary text
- Generates embeddings using Sentence Transformer models
- Creates structured JSON output
- Sends embedding data to Module 4 (Vector Database Storage)

---

# 2. Input Format
## Accepted Input
The module accepts JSON data generated from Module 2 (LLM Processing & Summarization Module).

---
## Input JSON Structure
```json
{
    "document_id": "DOC001",
    "page_number": 1,
    "content_type": "text",
    "original_content": "Artificial Intelligence is transforming industries.",
    "generated_summary": "AI is transforming industries through automation.",
    "summary_length": 52,
    "processing_status": "success"
}
```


# 3. Output Format

## Module Output

The module returns structured embedding data in JSON format for Module 4 (Vector Database Storage Module).

---

## Output JSON Structure

```json
{
    "document_id": "DOC001",
    "page_number": 1,
    "content_type": "text",
    "generated_summary": "AI is transforming industries through automation.",
    "embedding_model": "all-MiniLM-L6-v2",
    "embedding_dimension": 384,
    "embedding_vector": [0.123, -0.551, 0.771],
    "metadata": {
        "summary_length": 52,
        "timestamp": "2026-05-17T10:30:00"
    },
    "processing_status": "success"
}
```

---

# 4. Libraries / Technologies Used
## Programming Language

- Python 3.x

---

## Python Libraries

| Library | Purpose |
|---|---|
| sentence-transformers | Generate embeddings |
| torch | Backend deep learning support |
| numpy | Numerical operations |
| json | JSON data handling |

---

## Embedding Model Used

all-MiniLM-L6-v2

---

## APIs Used

- No external APIs required
- Local embedding generation

---

## Database

- No database used directly in this module
- Output is passed to Module 4 for Vector Database Storage

---

## Supported Vector Databases (Handled by Module 4)

- ChromaDB
- Pinecone
- FAISS
- Weaviate
- Milvus

---

# 5. How to Run

## Step 1 - Install Dependencies

Run the following command:

```bash
pip install -r requirements.txt
```

---

## Step 2 - Verify Input File

Ensure the input JSON file exists:

```text
input/sample_input.json
```

---

## Step 3 - Execute the Module

Run:

```bash
python main.py
```

---

## Step 4 - Output Generated

The generated embedding output will be saved in:

```text
output/sample_output.json
```

---

# Required Dependencies

## requirements.txt

```text
sentence-transformers
torch
numpy
```

---

# Module Workflow

```text
Module 2 Output
        ↓
Input Validation
        ↓
Text Preprocessing
        ↓
Embedding Generation
        ↓
JSON Formatting
        ↓
Output to Module 4
```

---

# Project Structure

```text
module3_embedding_generator/
│
├── main.py
├── config.py
├── requirements.txt
│
├── models/
│   └── embedding_model.py
│
├── services/
│   ├── embedding_service.py
│   ├── preprocessing_service.py
│   └── validation_service.py
│
├── utils/
│   ├── logger.py
│   ├── helpers.py
│   └── formatter.py
│
├── input/
│   └── sample_input.json
│
├── output/
│   └── sample_output.json
│
└── README.md
```

---

# Future Enhancements

- Batch embedding generation
- Multilingual embedding support
- GPU acceleration
- API integration
- Chunk-based embeddings
- Streaming pipeline support

---

# Contributor

Module 3 - Embedding Generation 