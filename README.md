# 🌐 RAG-Based Website Research Assistant

A Retrieval-Augmented Generation (RAG) powered web assistant that extracts content from websites and answers user queries using Large Language Models (LLMs).

---

## 🚀 Project Overview

This project allows users to:

- Input up to 3 website URLs
- Extract and process website content
- Store embeddings in a vector database (ChromaDB)
- Ask questions based only on the provided website content
- Get accurate, context-based answers with source references

The assistant ensures:
✔ No hallucination  
✔ Answers only from provided content  
✔ Source transparency  

---

## 🎯 Main Aim

To build an intelligent research assistant that:

- Automates website content analysis
- Uses RAG architecture for factual responses
- Avoids hallucinated outputs
- Provides source-backed answers

---

## 🧠 Basic Idea (How It Works)

1. User enters website URLs.
2. Website content is extracted using BeautifulSoup (via UnstructuredURLLoader).
3. Content is split into smaller chunks.
4. Chunks are converted into embeddings using HuggingFace models.
5. Embeddings are stored in ChromaDB.
6. When a user asks a question:
   - Relevant chunks are retrieved.
   - LLM (Groq - LLaMA model) generates answer strictly from retrieved content.
   - Sources are displayed.

---

## 🏗️ Tech Stack

### 🔹 Framework
- LangChain

### 🔹 LLM
- Groq (LLaMA 3.3-70B Versatile - Free Version)

### 🔹 Embeddings
- HuggingFace (sentence-transformers/all-MiniLM-L6-v2)

### 🔹 Vector Database
- ChromaDB

### 🔹 Frontend
- Streamlit

### 🔹 Data Extraction
- BeautifulSoup (via UnstructuredURLLoader)

### 🔹 Environment Management
- Python-dotenv

---


