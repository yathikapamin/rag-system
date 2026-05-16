## Multimodal RAG System

This project is a modular Multimodal Retrieval-Augmented Generation (RAG) system designed to process PDF documents, extract meaningful information, generate embeddings, and perform intelligent retrieval using Large Language Models (LLMs).

The system is divided into independent modules so that each component can be developed, tested, and maintained separately. Each module performs a dedicated task in the pipeline and communicates with other modules through structured outputs.

## Project Workflow
PDF Upload
    ↓
Module 1: PDF Extraction
    ↓
Module 2: LLM Processing & Summarization
    ↓
Module 3: Embedding Generation
    ↓
Module 4: Vector Database Storage
    ↓
Module 5: Orchestrator

## Modules Overview

 Module                                       Input                                                                  Output                                             

 Module 1 — PDF Extraction                 | PDF document uploaded by user                                         | Extracted text, page-wise images, page details     
 Module 2 — LLM Processing & Summarization | Output from Module 1 (text/images/page details)                       | Summarized text/content                            
 Module 3 — Embedding Generation           | Output from Module 2 (summarized text)                                | Embedding vectors                                  
 Module 4 — Vector Database Storage        | Output from Module 3 (embeddings) + summary + metadata + page details | Stored vector records in vector database           
 Module 5 — Orchestrator                   | Controls inputs/outputs of all modules                                | Complete pipeline execution and module integration 

## Important Instructions for Contributors

 Common Data Format

All modules should follow a common structured data format for smooth integration.

Example format:

{
    "document_name": "sample.pdf",
    "page": 1,
    "text": "Extracted text",
    "images": ["img1.png"],
    "summary": "Summarized content",
    "embedding": [0.12, 0.44, 0.91],
    "metadata": {
        "page_number": 1,
        "location": "Page 1"
    }
}

Each module is developed independently by a contributor/team member.

Every module folder must contain its own README.md file with the following details:

## Required Contents in Module README
1. Module Description

What the module does
Purpose of the module

2. Input Format

What input the module accepts
Input data structure/JSON format

3. Output Format

What output the module returns
Output JSON structure


4. Libraries/Technologies Used

Mention:

Python libraries
APIs
Models
Databases

5. How to Run

Installation steps
Execution command
Required dependencies
