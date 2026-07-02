# ADR 0001: Platform-First AI Copilot Architecture

## Status

Accepted

## Date

2026-07-02

## Context

The goal of Enterprise AI Copilot is to build a production-ready AI engineering portfolio project.

The project should not be a simple LLM API wrapper. A simple wrapper would only prove that the application can send prompts to a model. That is not enough for a serious AI engineering portfolio.

The project needs to demonstrate:

- RAG architecture
- Document ingestion
- Chunking strategies
- Dense retrieval
- Sparse retrieval
- Hybrid retrieval
- Grounded generation
- Verified citations
- Evaluation
- Observability
- Safety
- Agent permissions
- Model strategy decisions

The platform should start with one strong core product: Production RAG Copilot with Verified Citations.

Other modules should be added later as platform capabilities.

## Decision

We will build Enterprise AI Copilot as a platform-first monorepo.

The first deep product will be:

```text
Project 1: Production RAG Copilot with Verified Citations
```

The later platform modules will be:

```text
Project 14: Evaluation-as-a-Service Platform
Project 11: AI Trace Explorer for LLM Workflows
Project 6: Permissioned Tool-Using Agent Sandbox
Project 10: Fine-Tune vs RAG Decision Lab
```

The project will use provider boundaries so the system is not locked to one vendor.

Provider interfaces will be created for:

```text
LLM providers
Embedding providers
Vector stores
Rerankers
Eval judges
Trace collectors
```

The model will be treated as one component inside a controlled engineering system.

## Architecture Choice

The project will use this structure:

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

## Current Implementation Decision

The current completed implementation includes:

```text
Phase 0
Phase 1A
Phase 1B
```

Current RAG foundation:

```text
Upload file
-> Load document
-> Generate document metadata
-> Generate stable document ID
-> Chunk document
-> Generate stable chunk IDs
-> Embed chunks
-> Store vectors in Qdrant
-> Search semantically
```

## Technology Decisions

### API

Decision:

```text
FastAPI
```

Reason:

* Strong Python ecosystem
* Good OpenAPI docs
* Good Pydantic integration
* Suitable for AI service APIs

### Package Manager

Decision:

```text
uv
```

Reason:

* Fast dependency management
* Modern Python workflow
* Good for reproducible project setup

### Schemas

Decision:

```text
Pydantic v2
```

Reason:

* Strong typed contracts
* Useful for LLM output validation
* Useful for API request and response validation
* Useful for tool schemas later

### Embeddings

Decision:

```text
Sentence Transformers with BGE model
```

Default:

```text
BAAI/bge-small-en-v1.5
```

Reason:

* Free-first
* Local development friendly
* Good enough for portfolio RAG
* Can be replaced later through provider interface

### Vector Database

Decision:

```text
Qdrant
```

Reason:

* Strong vector search database
* Easy Docker setup
* Good metadata payload support
* Good production-style choice
* Can be replaced later through vector store interface

### LLM

Decision:

```text
DeepSeek through provider adapter
```

Reason:

* Cost-effective hosted LLM option
* OpenAI-compatible API style
* Good for chat and reasoning flows
* Can be swapped later because business logic will use provider interface

### Local LLM Fallback

Decision:

```text
Ollama later
```

Reason:

* Free local demo path
* Avoids full dependency on hosted provider
* Useful for low-risk local testing

## Consequences

### Positive Consequences

* Project looks like a real AI engineering system
* Business logic does not depend directly on one vendor
* Components can be tested separately
* RAG pipeline can improve step by step
* Evaluation and observability can be added naturally
* Agent module can reuse the same trace and eval platform
* Fine-tune decision lab can reuse eval infrastructure

### Negative Consequences

* More code than a simple LLM wrapper
* More setup complexity
* Requires careful documentation
* Requires tests to avoid becoming messy
* Requires consistent schemas across modules

## Rules

### LLM Boundary Rule

Business logic must not call DeepSeek directly.

Allowed:

```text
business logic -> LLM provider interface -> DeepSeek adapter
```

Not allowed:

```text
business logic -> direct DeepSeek API call
```

### Embedding Boundary Rule

RAG logic must not depend directly on Sentence Transformers.

Allowed:

```text
indexing service -> EmbeddingProvider -> SentenceTransformersEmbeddingProvider
```

### Vector Store Boundary Rule

RAG logic must not depend directly on Qdrant-specific code.

Allowed:

```text
retrieval service -> VectorStore -> QdrantVectorStore
```

### Secrets Rule

Secrets must come from environment variables.

Not allowed:

```text
committed .env
hard-coded API key
hard-coded model endpoint
```

### Traceability Rule

Every production workflow should eventually return:

```text
trace_id
prompt_version
model
retrieval_strategy
chunker_version
embedding_model
latency_ms
```

### Evaluation Rule

No AI feature is considered production-ready until it has measurable evaluation.

## Current Status

Accepted and actively implemented.

## Next Decision Needed

ADR 0002 should define the hybrid retrieval strategy:

```text
BM25 + Qdrant dense retrieval + RRF fusion
```
