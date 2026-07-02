# Architecture

## System Goal

Enterprise AI Copilot is a production-style AI platform starting with a RAG copilot and expanding into evaluation, tracing, safe agents, and model decision workflows.

The core product is Project 1: Production RAG Copilot with Verified Citations.

The system is designed to show real AI engineering skills, not only prompt engineering.

## Current Architecture Status

Current completed level:

```text
Phase 0
Phase 1A
Phase 1B
```

Current working architecture:

```text
Client or Swagger UI
-> FastAPI API
-> Ingestion service
-> Loader
-> Chunker
-> Embedding provider
-> Qdrant vector store
-> Semantic retriever
-> Search response
```

## High-Level Target Architecture

```text
Client/UI
  |
  v
FastAPI API
  |
  |-- Ingestion Service
  |     |-- Loaders
  |     |-- Normalizers
  |     |-- Chunkers
  |     |-- Embedding Provider
  |     |-- Vector Store
  |
  |-- Retrieval Service
  |     |-- Dense Search
  |     |-- Sparse Search
  |     |-- RRF Fusion
  |     |-- Reranking
  |
  |-- Generation Service
  |     |-- LLM Provider Interface
  |     |-- DeepSeek Adapter
  |     |-- Grounded Answer Contract
  |
  |-- Verification Service
  |     |-- Claim Extraction
  |     |-- Citation Support Check
  |     |-- Confidence Score
  |
  |-- Evaluation Service
  |     |-- Golden Test Set
  |     |-- Retrieval Metrics
  |     |-- Answer Metrics
  |     |-- Citation Metrics
  |
  |-- Observability
        |-- Trace IDs
        |-- Spans
        |-- Logs
        |-- Metrics
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

## Current Implemented Components

### FastAPI API

Location:

```text
apps/api/
```

Responsibilities:

* Expose API routes
* Validate requests
* Return typed responses
* Provide `/health`
* Provide ingestion endpoints
* Provide semantic retrieval endpoint

Current endpoints:

```text
GET /health
POST /v1/ingest/files/preview
POST /v1/ingest/files
POST /v1/retrieval/search
```

### Config System

Location:

```text
packages/core/config.py
```

Responsibilities:

* Load environment variables
* Centralize app settings
* Avoid hard-coded provider names and URLs
* Prepare system for DeepSeek, Qdrant, database, tracing, and eval services

Current settings include:

```text
APP_NAME
APP_ENV
EMBEDDING_MODEL
QDRANT_URL
QDRANT_COLLECTION_NAME
```

Planned settings include:

```text
DEEPSEEK_API_KEY
LLM_BASE_URL
LLM_CHAT_MODEL
LLM_REASONER_MODEL
DATABASE_URL
REDIS_URL
TRACE_COLLECTOR_URL
EVAL_SERVICE_URL
```

### Document Loader

Location:

```text
packages/core/rag/loaders.py
```

Current responsibilities:

* Load `.txt`
* Load `.md`
* Load `.markdown`
* Decode UTF-8 content
* Validate empty content
* Generate document content hash
* Generate stable document ID
* Preserve metadata

Future responsibilities:

* PDF loader
* HTML loader
* Metadata from page numbers
* Source timestamp extraction
* Version and access-level extraction

### Chunker

Location:

```text
packages/core/rag/chunking.py
```

Current chunking strategy:

```text
fixed_word_overlap_chunker v1
```

Current responsibilities:

* Split document into word-based chunks
* Add overlap between chunks
* Generate stable chunk IDs
* Generate chunk hashes
* Preserve chunker name and version
* Preserve document metadata in chunks

Future chunking strategies:

* Heading-aware chunking
* Markdown section chunking
* PDF page-aware chunking
* Semantic chunking
* Chunk strategy comparison through evals

### Embedding Provider

Location:

```text
packages/embedding_providers/
```

Current provider:

```text
SentenceTransformersEmbeddingProvider
```

Current model:

```text
BAAI/bge-small-en-v1.5
```

Responsibilities:

* Load embedding model lazily
* Generate normalized embeddings
* Expose embedding dimension
* Return vectors as plain Python lists

Future providers:

* OpenAI-compatible embeddings
* DeepSeek-compatible embeddings if available
* Local model fallback
* Cached embeddings

### Vector Store

Location:

```text
packages/vector_stores/
```

Current store:

```text
QdrantVectorStore
```

Responsibilities:

* Ensure collection exists
* Upsert vector records
* Search by query vector
* Return typed search results
* Preserve chunk metadata in payload

Future stores:

* Chroma
* pgvector
* Hybrid metadata store linked with Postgres

### Indexing Service

Location:

```text
packages/core/rag/indexing.py
```

Responsibilities:

* Ingest file bytes
* Chunk document
* Embed chunks
* Create vector records
* Upsert into Qdrant
* Return indexing result

Current output includes:

```text
document_id
title
source_uri
chunk_count
indexed_chunk_ids
embedding_model
vector_collection
```

### Semantic Retriever

Location:

```text
packages/core/rag/retrieval.py
```

Responsibilities:

* Embed user query
* Search Qdrant
* Return top-k semantic results
* Support metadata filters

Current output includes:

```text
query
top_k
results
embedding_model
vector_collection
```

## Data Contracts

### Document

Fields:

```text
document_id
source_uri
title
doc_type
content
content_hash
access_level
metadata
```

### Chunk

Fields:

```text
chunk_id
document_id
document_title
source_uri
chunk_index
chunk_text
chunk_hash
chunker
chunker_version
token_count_estimate
embedding_model
metadata
```

### Vector Record

Fields:

```text
id
text
vector
metadata
```

### Vector Search Result

Fields:

```text
chunk_id
score
text
metadata
```

## Current Data Flow

### Ingestion Preview

```text
POST /v1/ingest/files/preview
  |
  v
load_text_document_from_bytes
  |
  v
chunk_document
  |
  v
return document + chunks
```

### Ingest and Index

```text
POST /v1/ingest/files
  |
  v
DocumentIndexer
  |
  v
load document
  |
  v
chunk document
  |
  v
generate embeddings
  |
  v
ensure Qdrant collection
  |
  v
upsert vectors
  |
  v
return indexing result
```

### Semantic Search

```text
POST /v1/retrieval/search
  |
  v
SemanticRetriever
  |
  v
embed query
  |
  v
search Qdrant
  |
  v
return ranked chunks
```

## Target RAG Flow

```text
User question
  |
  v
Create trace ID
  |
  v
Dense retrieval from Qdrant
  |
  v
Sparse retrieval from BM25
  |
  v
RRF fusion
  |
  v
Optional reranking
  |
  v
Context selection
  |
  v
DeepSeek grounded generation
  |
  v
Structured answer validation
  |
  v
Claim extraction
  |
  v
Citation verification
  |
  v
Confidence scoring
  |
  v
Final answer with citations and trace ID
```

## Planned Database Model

PostgreSQL will eventually store durable metadata.

Planned tables:

```text
documents
chunks
retrieval_runs
questions
answers
citations
eval_cases
feedback
traces
span_events
```

## Planned Document Table

```text
documents(
  id,
  source_uri,
  title,
  doc_type,
  access_level,
  version,
  last_updated,
  hash,
  status,
  created_at,
  updated_at
)
```

## Planned Chunks Table

```text
chunks(
  id,
  document_id,
  section,
  page,
  chunk_text,
  chunk_hash,
  embedding_model,
  chunker,
  chunker_version,
  token_count,
  created_at
)
```

## Planned Retrieval Runs Table

```text
retrieval_runs(
  id,
  question_id,
  strategy,
  top_k,
  latency_ms,
  raw_scores_json,
  created_at
)
```

## Provider Boundaries

The project uses provider interfaces so business logic does not depend on a single vendor.

Current providers:

```text
EmbeddingProvider
VectorStore
```

Planned providers:

```text
LLMProvider
RerankerProvider
TraceProvider
EvalProvider
```

## Security Principles

* Never commit `.env`
* Secrets come from environment variables
* API keys are not hard-coded
* Payload redaction will be added before trace storage
* Access-level metadata is already present in chunks
* Role-based filtering will be added later
* High-risk agent actions will require deterministic permission checks

## Observability Principles

Every production workflow should eventually include:

```text
trace_id
prompt_version
model
embedding_model
retrieval_strategy
chunker_version
latency_ms
cost_estimate
error_type
safety_verdict
eval_verdict
```

Current status:

```text
Observability folder exists or is planned.
Trace ID implementation is not yet completed.
```

## Quality Principles

The system must be measurable.

Future metrics:

```text
retrieval_recall_at_5
mean_reciprocal_rank
citation_precision
answer_correctness
refusal_accuracy
p95_latency
estimated_cost
```

## Deployment Direction

Current local services:

```text
FastAPI
Qdrant
```

Planned Docker Compose services:

```text
api
worker
dashboard
postgres
redis
qdrant
minio
jaeger
prometheus
grafana
```

## Architecture Rule

The model is not the product. The production system around the model is the product.
