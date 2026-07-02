# Enterprise AI Copilot

Production-ready AI engineering portfolio project focused on building a real RAG copilot platform with verified citations, evaluation, observability, safe agents, and model decision workflows.

This is not a simple LLM wrapper. The goal is to build the engineering system around the model: ingestion, retrieval, chunking, embeddings, citation support, evaluation, tracing, safety, deployment, monitoring, rollback thinking, and cost control.

## Current Status

Phase 0: Completed  
Phase 1A: Completed  
Phase 1B: Completed  
Next: Phase 1C, Hybrid Retrieval with BM25 + RRF

## What Is Completed

- Professional monorepo structure created
- FastAPI backend created
- `/health` endpoint added
- Shared config system added
- Environment variable based settings added
- Document ingestion preview added
- Text and Markdown loader added
- Stable document IDs added
- Stable chunk IDs added
- Content hashing added
- Fixed word overlap chunking added
- Chunk metadata preserved
- Sentence Transformers embedding provider added
- Qdrant vector store adapter added
- Qdrant indexing added
- Semantic retrieval endpoint added
- Docker Compose added for Qdrant

## Current RAG Flow

```text
Upload file
-> Load document
-> Create metadata
-> Generate stable document ID
-> Split into chunks
-> Generate stable chunk IDs
-> Generate embeddings
-> Store vectors in Qdrant
-> Search semantically
```

## Project Structure

```text
enterprise-ai-copilot/
├── apps/
│   ├── api/
│   ├── worker/
│   └── dashboard/
│
├── packages/
│   ├── core/
│   ├── llm_providers/
│   ├── embedding_providers/
│   ├── vector_stores/
│   ├── schemas/
│   └── observability/
│
├── infra/
│   ├── docker/
│   ├── postgres/
│   ├── qdrant/
│   └── redis/
│
├── datasets/
│   ├── sample_docs/
│   └── eval_sets/
│
├── docs/
│   ├── architecture.md
│   ├── roadmap.md
│   └── decisions/
│
├── tests/
├── .env.example
├── docker-compose.yml
├── Makefile
├── README.md
└── pyproject.toml
```

## Tech Stack

### Backend

* Python
* FastAPI
* Pydantic v2
* uv

### Embeddings

* Sentence Transformers
* Default model: `BAAI/bge-small-en-v1.5`

### Vector Database

* Qdrant

### Planned LLM Layer

* DeepSeek through OpenAI-compatible adapter
* Ollama local fallback later

### Planned Storage

* PostgreSQL
* Alembic migrations
* MinIO or local file storage

### Planned Queue

* Redis
* Celery, RQ, or Arq

### Planned Observability

* Trace ID per request
* OpenTelemetry style spans
* Jaeger or Langfuse/Phoenix OSS later
* Prometheus/Grafana later

## Environment Variables

Create `.env` from `.env.example`.

```env
APP_NAME=Enterprise AI Copilot
APP_ENV=local
API_HOST=0.0.0.0
API_PORT=8000

DEEPSEEK_API_KEY=
LLM_BASE_URL=
LLM_CHAT_MODEL=
LLM_REASONER_MODEL=
LOCAL_FALLBACK_MODEL=

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5

QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION_NAME=rag_chunks_v1

DATABASE_URL=
REDIS_URL=
TRACE_COLLECTOR_URL=
EVAL_SERVICE_URL=
```

Important: never commit `.env`.

## Run Qdrant

```bash
docker compose up -d qdrant
```

## Run API

```bash
uv run uvicorn apps.api.main:app --reload
```

Open API docs:

```text
http://127.0.0.1:8000/docs
```

## Current API Endpoints

### Health

```text
GET /health
```

### Ingestion Preview

```text
POST /v1/ingest/files/preview
```

Use this to upload a `.txt`, `.md`, or `.markdown` file and preview chunks without indexing.

### Ingest and Index

```text
POST /v1/ingest/files
```

Use this to upload a file, chunk it, embed chunks, and index them into Qdrant.

### Semantic Search

```text
POST /v1/retrieval/search
```

Example body:

```json
{
  "query": "What is the refund policy?",
  "top_k": 5
}
```

## Roadmap Summary

### Phase 0: Foundation

Status: Completed

* Repo setup
* Project structure
* FastAPI app
* Config system
* Documentation
* Base dependencies

### Phase 1A: Document Ingestion and Chunking

Status: Completed

* Text and Markdown file loading
* Metadata extraction
* Content hashing
* Stable IDs
* Fixed overlap chunking
* Chunk metadata

### Phase 1B: Embeddings and Qdrant Semantic Retrieval

Status: Completed

* Sentence Transformers embedding provider
* Qdrant vector store adapter
* Vector indexing
* Semantic search endpoint

### Phase 1C: Hybrid Retrieval

Status: Next

* BM25 sparse retrieval
* Dense retrieval from Qdrant
* Reciprocal Rank Fusion
* Retrieval run metadata
* Retrieval strategy comparison

### Phase 1D: DeepSeek Grounded Answer Generation

Status: Planned

* LLM provider interface
* DeepSeek adapter
* Strict grounded answer prompt
* Structured answer schema
* Refusal behavior when context is insufficient

### Phase 1E: Citations

Status: Planned

* Citation objects
* Chunk-linked claims
* Answer rendering with citations
* Source metadata in response

### Phase 1F: Citation Verification

Status: Planned

* Claim extraction
* Citation support checking
* Confidence scoring
* Unsupported claim detection

### Phase 1G: Evaluation

Status: Planned

* Golden eval set
* Retrieval recall@k
* Citation precision
* Refusal accuracy
* Regression report

### Phase 1H: Observability

Status: Planned

* Trace ID for every workflow
* Retrieval traces
* Prompt traces
* Model call traces
* Error and latency tracking

## Long-Term Platform Modules

After Project 1 is strong, the platform will expand into:

1. Evaluation-as-a-Service
2. AI Trace Explorer
3. Permissioned Tool-Using Agent Sandbox
4. Fine-Tune vs RAG Decision Lab

## Production Principles

* Never call an LLM directly from business logic
* Use provider interfaces for LLMs, embeddings, and vector stores
* Every answer should eventually return a `trace_id`
* Every answer should include citation metadata
* Every eval run should be reproducible
* Every prompt should have a version
* Every model should be configured through environment variables
* Secrets must never be committed
* Store enough metadata to debug failures later
* Build for replacement, not vendor lock-in

## Commit Status

Latest completed feature:

```text
Embeddings, Qdrant indexing, and semantic retrieval
```

Next commit should be:

```text
Add BM25 sparse retrieval and RRF hybrid fusion
```
