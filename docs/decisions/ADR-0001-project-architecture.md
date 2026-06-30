# ADR-0001: Use Modular Enterprise AI Platform Architecture

## Status

Accepted

## Context

The project is a production-ready AI engineering portfolio platform.

The goal is not to build a simple chatbot. The goal is to build a professional company-grade AI platform with:
- RAG
- Verified citations
- Evaluations
- Tracing
- Safe agent actions
- Model decision experiments

The system must be scalable and replaceable.

## Decision

We will use a modular architecture.

External systems will be accessed through adapters.

The first version will use:
- FastAPI for backend
- Supabase managed PostgreSQL for database
- DeepSeek as the first LLM provider
- Qdrant or Chroma for vector search later
- Streamlit for early UI
- uv for Python environment management

## Why

This architecture allows replacing tools later without rewriting the whole system.

Examples:
- DeepSeek can be replaced with OpenAI or Ollama
- Qdrant can be replaced with Chroma or pgvector
- Streamlit can be replaced with React
- Supabase can be replaced with another PostgreSQL provider

## Consequences

Benefits:
- Clean architecture
- Better learning
- Easier debugging
- Better interview story
- More professional GitHub repo

Tradeoff:
- Slightly slower at the beginning because we create structure first