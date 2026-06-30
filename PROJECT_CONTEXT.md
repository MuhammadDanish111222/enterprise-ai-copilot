# Enterprise AI Copilot Platform - Project Context

## Project Goal

Build a professional, production-ready enterprise AI platform for a company.

The platform will support:
- Admins
- Employees
- Customers
- Managers
- Support teams

This is not a simple chatbot. It is a scalable AI engineering platform with RAG, verified citations, evaluations, tracing, safe agents, and model decision experiments.

## Core Product

The main product is a Production RAG Copilot with verified citations.

The user asks a question, and the system:
1. Checks user role and permissions
2. Retrieves allowed company knowledge
3. Generates an answer using an LLM
4. Returns citations
5. Verifies citation support
6. Stores trace logs
7. Allows feedback and evaluation

## Main Modules

1. Production RAG Copilot
2. Evaluation Module
3. Trace / Observability Module
4. Permissioned Agent Module
5. Fine-tune vs RAG Decision Lab

## Architecture Principles

- Everything must be modular and replaceable.
- LLM provider must be behind an adapter.
- Embedding provider must be behind an adapter.
- Vector database must be behind an adapter.
- Database access must be separated from business logic.
- API routes must not contain business logic.
- Secrets must come from environment variables.
- Every workflow should have a trace_id.
- The model should never directly control business logic.
- Deterministic code should handle permissions, validation, policies, and execution.

## Current Tech Stack

- OS: Windows
- Python manager: uv
- Backend: FastAPI
- Config: Pydantic Settings
- Database: Supabase managed PostgreSQL
- LLM: DeepSeek first, replaceable later
- Vector DB: Qdrant or Chroma later
- UI: Streamlit first
- Deployment: Docker Compose later
- Version control: Git + GitHub

## How ChatGPT Should Help

Before starting any module:
1. Teach the concept first
2. Explain why it exists in production
3. Explain how it connects with the platform
4. Give architecture before code
5. Give step-by-step implementation
6. Give testing steps
7. Give Git commit message

Always keep the project professional, scalable, and beginner-friendly.