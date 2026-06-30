# Architecture

## High-Level Architecture

The platform is designed as a modular enterprise AI system.

User
→ API Layer
→ Auth / Permissions
→ Business Services
→ Provider Adapters
→ External Systems

## Main Components

### API Layer

FastAPI handles:
- HTTP requests
- API versioning
- Request validation
- Response formatting

API routes should not contain business logic.

### Core Services

Core services handle:
- RAG workflow
- Document processing
- Answer generation
- Citation verification
- Evaluation
- Tracing
- Agent workflows

### Provider Adapters

Adapters make external tools replaceable.

Examples:
- DeepSeek adapter
- Ollama adapter
- OpenAI adapter
- Qdrant adapter
- Chroma adapter
- Supabase database adapter

### Database

Supabase managed PostgreSQL will store:
- users
- organizations
- documents
- chunks
- questions
- answers
- citations
- traces
- feedback
- eval cases

### Vector Store

Vector DB will store document chunk embeddings.

Default planned option:
- Qdrant

Possible replacements:
- Chroma
- pgvector
- Pinecone

### LLM Provider

Default:
- DeepSeek

Possible replacements:
- OpenAI
- Ollama
- Gemini
- Claude

LLM must always be accessed through an internal adapter.

## Replaceability Rule

No business logic should directly call:
- DeepSeek
- Qdrant
- Supabase
- Redis
- Any external API

Business logic should call internal interfaces only.