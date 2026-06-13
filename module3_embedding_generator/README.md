# Module 3 - Embedding Generation Module

## Project Overview

The Embedding Generation Module is the third component of the Retrieval-Augmented Generation (RAG) System.

This module receives summarized content from Module 2 (Summarization Module) and converts the summary into numerical vector embeddings using a pre-trained transformer model.

These embeddings are then passed to Module 4 (Vector Database Storage Module) for indexing and semantic retrieval.

---

## Objective

The primary objective of this module is to transform human-readable summaries into machine-understandable vector representations that can be efficiently stored and searched in a vector database.

---

## Module Position in RAG Pipeline

```
PDF Document
      ↓
Module 1 - PDF Extraction
      ↓
Module 2 - Summarization
      ↓
Module 3 - Embedding Generation
      ↓
Module 4 - Vector Database Storage
      ↓
Module 5 - Orchestrator / Retrieval
```

---

## Features

- Validates incoming data
- Cleans and preprocesses summary text
- Generates semantic embeddings using transformer models
- Supports content from:
  - Text
  - Images
  - Tables
  - Figures
  - OCR Documents
  - Mixed PDF Content
- Produces structured JSON output
- Ready for Vector Database Integration

---

## Folder Structure

```text
module3/
│
├── embedding_module.py
├── main.py
├── sample_input.json
├── sample_output.json
├── requirements.txt
└── README.md
```

---

## Components Description

### 1. ValidationService

Responsible for validating the input data.

Functions:
- Checks mandatory fields
- Verifies summary availability
- Prevents invalid input processing

---

### 2. PreprocessingService

Responsible for cleaning text before embedding generation.

Functions:
- Remove extra spaces
- Normalize text formatting
- Improve embedding quality

---

### 3. EmbeddingService

Responsible for generating embeddings.

Functions:
- Load transformer model
- Convert summary text into vector representation
- Generate semantic embeddings

Model Used:

```
sentence-transformers/all-MiniLM-L6-v2
```

Embedding Dimension:

```
384
```

---

### 4. Formatter

Responsible for formatting final output.

Functions:
- Create structured JSON response
- Add metadata
- Add embedding information

---

### 5. EmbeddingGenerator

Main controller class.

Functions:
- Coordinate all services
- Execute complete embedding pipeline
- Return final output

---

## Input Format

The module accepts JSON input from Module 2.

### Sample Input

```json
{
    "document_id": "DOC001",
    "page_number": 1,
    "content_type": "text",
    "generated_summary": "Artificial Intelligence is transforming industries through automation and machine learning."
}
```

---

## Supported Content Types

### Text

```json
{
    "content_type": "text"
}
```

### Image

```json
{
    "content_type": "image"
}
```

### Table

```json
{
    "content_type": "table"
}
```

### Figure

```json
{
    "content_type": "figure"
}
```

### OCR Content

```json
{
    "content_type": "ocr"
}
```

### Mixed Content

```json
{
    "content_type": "mixed"
}
```

---

## Output Format

### Sample Output

```json
{
    "document_id": "DOC001",
    "page_number": 1,
    "content_type": "text",
    "generated_summary": "Artificial Intelligence is transforming industries through automation and machine learning.",
    "embedding_dimension": 384,
    "embedding_vector": [
        0.123,
        -0.456,
        0.789
    ],
    "processing_status": "success",
    "timestamp": "2026-06-12T12:00:00"
}
```

---

## Output Fields Description

| Field | Description |
|---------|-------------|
| document_id | Unique document identifier |
| page_number | PDF page number |
| content_type | Type of extracted content |
| generated_summary | Summary received from Module 2 |
| embedding_dimension | Size of embedding vector |
| embedding_vector | Numerical vector representation |
| processing_status | Success or Failure |
| timestamp | Processing time |

---

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Required Libraries

```text
transformers
torch
numpy
```

---

## Execution

Run the module using:

```bash
python main.py
```

---

## Expected Output

```text
Loading embedding model...
Embedding generation successful.
```

---

## Workflow

### Step 1

Read input JSON.

### Step 2

Validate input data.

### Step 3

Clean summary text.

### Step 4

Generate embedding vector.

### Step 5

Format output.

### Step 6

Save output JSON.

---

## Integration with Module 4

This module provides the following output to Module 4:

- Document ID
- Page Number
- Content Type
- Summary
- Embedding Vector
- Metadata

Module 4 stores this information in a Vector Database for semantic search and retrieval.

---

## Future Enhancements

- Support for multiple embedding models
- Batch embedding generation
- GPU acceleration
- Hybrid embeddings
- Multilingual embeddings
- Vector database direct integration

---

## Developed For

Retrieval-Augmented Generation (RAG) System Project

Module 3: Embedding Generation Module

Team Project – AI Based Document Retrieval System