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

Module 1	Reads PDF documents, extracts text and images page-wise
Module 2	Sends extracted content to LLM for summarization
Module 3	Converts summarized text into embeddings
Module 4	Stores embeddings and metadata in vector database
Module 5	Orchestrates and manages the complete workflow
Important Instructions for Contributors

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
