# 🚀 Knowledge Graph RAG System
### Enterprise Hybrid Retrieval-Augmented Generation Platform

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-pgvector-blue)
![Neo4j](https://img.shields.io/badge/Neo4j-KnowledgeGraph-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Groq](https://img.shields.io/badge/Groq-LLM-red)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

---

# Executive Summary

Knowledge Graph RAG is an end-to-end Retrieval-Augmented Generation platform that combines **semantic vector retrieval** with **graph-based reasoning** to provide richer and more explainable responses from large document collections.

Unlike conventional RAG systems that rely solely on vector similarity, this project augments semantic retrieval with a knowledge graph extracted from the source documents. The resulting architecture enables contextual retrieval, relationship-aware reasoning, and structured knowledge exploration.

The system is designed as a modular AI backend using FastAPI and integrates PostgreSQL with pgvector, Neo4j, Sentence Transformers, and Groq LLMs.

---

# Why This Project Exists

Traditional Retrieval-Augmented Generation systems retrieve only semantically similar document chunks.

They cannot answer questions such as:

- How are two concepts related?
- Which entities depend on each other?
- What hierarchy exists inside the document?
- What components belong to a system?

A Knowledge Graph solves these limitations.

This project combines both approaches.

```
          User Question
                │
                ▼
        Hybrid Retrieval Engine
       ┌──────────┴──────────┐
       ▼                     ▼
 Vector Search         Graph Search
(PostgreSQL)             (Neo4j)
       │                     │
       └──────────┬──────────┘
                  ▼
          Context Fusion Layer
                  │
                  ▼
            Groq LLM Reasoning
                  │
                  ▼
            Final AI Response
```

---

# Key Features

- Hybrid Retrieval (Vector + Graph)
- PDF Document Ingestion
- Semantic Search using pgvector
- Knowledge Graph Construction
- Entity Extraction using LLM
- Relationship Extraction
- Neo4j Graph Database
- FastAPI REST Backend
- Swagger API Documentation
- Dockerized Infrastructure
- Modular Project Architecture

---

# Technology Stack

| Layer | Technology |
|---------|------------|
| Backend | FastAPI |
| Language | Python 3.12 |
| Vector Database | PostgreSQL + pgvector |
| Graph Database | Neo4j |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| LLM | Groq Llama 3.3 70B |
| PDF Parsing | pypdf |
| Text Splitting | LangChain RecursiveCharacterTextSplitter |
| ORM | SQLAlchemy |
| Containerization | Docker |

---

# System Architecture

```
                           User

                             │

                             ▼

                    FastAPI REST API

                             │

        ┌────────────────────┼────────────────────┐

        ▼                    ▼                    ▼

     /upload             /chat              /health

        │                    │

        ▼                    ▼

  Document Pipeline     Hybrid Retrieval

        │                    │

        ▼                    ▼

 PostgreSQL + pgvector      Neo4j

        │                    │

        └──────────────┬─────┘

                       ▼

                  Groq LLM

                       ▼

                AI Generated Answer
```

---

# Retrieval Pipeline

## Step 1

User uploads a PDF.

↓

The document is parsed into raw text.

↓

The text is divided into overlapping chunks.

↓

Each chunk is embedded using Sentence Transformers.

↓

Embeddings are stored inside PostgreSQL using pgvector.

↓

The user submits a question.

↓

The question is converted into an embedding.

↓

Nearest document chunks are retrieved using vector similarity.

↓

The retrieved context is passed to the language model.

↓

The model generates the final answer.

---

# Knowledge Graph Pipeline

```
PDF

 │

 ▼

Text Extraction

 │

 ▼

Entity Extraction

 │

 ▼

Relationship Extraction

 │

 ▼

Neo4j Graph Database

 │

 ▼

Graph Query Engine
```

Entities represent important technical concepts.

Relationships connect those concepts into an explorable graph.

---

# Project Structure

```
app/

├── api/

├── core/

├── database/

├── graph/

├── ingestion/

├── retrieval/

├── models/

├── services/

├── utils/

└── main.py

data/

docker/

tests/
```

---

# REST API

## Health Check

GET

```
/health
```

Returns application status.

---

## Upload Document

POST

```
/upload
```

Uploads a PDF for ingestion.

---

## Chat

POST

```
/chat
```

Accepts a user question.

Performs hybrid retrieval.

Generates an AI answer.

---

# Engineering Decisions

This project intentionally separates the following responsibilities:

- Document ingestion
- Embedding generation
- Vector storage
- Knowledge graph construction
- Retrieval
- LLM reasoning

This modular design simplifies testing, maintenance, and future scalability.

---

# Current Capabilities

✔ PDF ingestion

✔ Text chunking

✔ Embedding generation

✔ PostgreSQL vector storage

✔ Semantic retrieval

✔ Entity extraction

✔ Relationship extraction

✔ Neo4j knowledge graph

✔ Hybrid retrieval

✔ AI-powered question answering

✔ Dockerized databases

✔ FastAPI backend

---

# Future Enhancements

- Background ingestion jobs for large documents
- Incremental graph updates
- Streaming LLM responses
- Authentication and user management
- Multi-document collections
- Graph visualization dashboard
- Observability and metrics
- Kubernetes deployment
- CI/CD pipeline
- Caching for retrieval results

---

# Design Philosophy

The goal of this project is not only to answer questions but also to preserve and expose the relationships within technical knowledge.

By combining semantic retrieval with graph reasoning, the system demonstrates how modern AI applications can move beyond keyword search toward structured, explainable retrieval.

---

# License

MIT License

---

## Acknowledgements

This project uses open-source technologies including FastAPI, PostgreSQL, pgvector, Neo4j, LangChain text splitters, Sentence Transformers, and Groq's language models.