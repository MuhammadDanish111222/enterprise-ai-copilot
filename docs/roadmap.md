# Roadmap

## Product Direction

Enterprise AI Copilot is a production-ready AI engineering portfolio project.

The build order is:

1. Production RAG Copilot with Verified Citations
2. Evaluation-as-a-Service Platform
3. AI Trace Explorer for LLM Workflows
4. Permissioned Tool-Using Agent Sandbox
5. Fine-Tune vs RAG Decision Lab

The current focus is Project 1. The other modules should not be started until Project 1 has a strong production foundation.

## Current Status

```text
Phase 0: Completed
Phase 1A: Completed
Phase 1B: Completed
Phase 1C: Next
```

## Phase 0: Foundation

Status: Completed

### Goal

Create the professional project foundation.

### Completed Items

* Repository created
* Professional folder structure created
* FastAPI backend initialized
* `/health` endpoint added
* Shared config system added
* Environment variable setup added
* Core package structure created
* Schema package structure created
* Provider package structure created
* Docs added
* Roadmap added
* Architecture direction added
* Docker Compose started with Qdrant

### Acceptance Criteria

* Project can be opened by another engineer and understood
* API can start locally
* Health endpoint works
* Settings are loaded from environment variables
* No secrets are hard-coded

### Status

Completed.

## Phase 1A: Document Ingestion and Chunking

Status: Completed

### Goal

Build the first RAG foundation: load files, normalize content, create metadata, and split documents into chunks.

### Completed Items

* Text file loader
* Markdown file loader
* UTF-8 validation
* Empty file validation
* Stable document ID generation
* Document content hashing
* Stable chunk ID generation
* Chunk hashing
* Fixed word overlap chunker
* Chunker name stored
* Chunker version stored
* Token count estimate stored
* Chunk metadata preserved
* Ingestion preview endpoint added

### API Added

```text
POST /v1/ingest/files/preview
```

### Acceptance Criteria

* A `.txt` or `.md` file can be uploaded
* File content is loaded correctly
* Document metadata is returned
* Chunks are returned
* Chunk count is returned
* Chunk IDs are stable
* Chunker version is visible in output

### Status

Completed.

## Phase 1B: Embeddings and Qdrant Semantic Retrieval

Status: Completed

### Goal

Index chunks into a real vector database and retrieve relevant chunks by semantic search.

### Completed Items

* Sentence Transformers embedding provider
* Embedding provider interface
* Default BGE embedding model configured
* Qdrant vector store adapter
* Vector store interface
* Qdrant collection creation
* Vector upsert
* Vector search
* Metadata stored in Qdrant payload
* Ingest and index endpoint added
* Semantic retrieval endpoint added
* Qdrant Docker Compose service added

### API Added

```text
POST /v1/ingest/files
POST /v1/retrieval/search
```

### Acceptance Criteria

* File can be uploaded and indexed
* Chunks are embedded
* Vectors are stored in Qdrant
* Query can be embedded
* Relevant chunks can be retrieved
* Search response includes score, text, and metadata
* Embedding model and collection name are included in response

### Status

Completed.

## Phase 1C: Hybrid Retrieval with BM25 and RRF

Status: Next

### Goal

Move from simple semantic search to production-style hybrid retrieval.

### Why This Matters

Dense retrieval can miss exact keywords, IDs, product names, policy names, and rare terms. Sparse retrieval can capture exact matches. RRF fusion combines both into a stronger retrieval strategy.

### Planned Items

* Add sparse retrieval module
* Add BM25 index over chunks
* Persist indexed chunks for sparse search
* Add hybrid retrieval service
* Add RRF fusion
* Return dense score, sparse score, and fused score
* Add retrieval strategy field
* Add retrieval debug output
* Add `/v1/retrieval/hybrid-search`

### Planned API

```text
POST /v1/retrieval/hybrid-search
```

### Planned Request

```json
{
  "query": "What is the refund policy?",
  "top_k": 5,
  "filters": {
    "access_level": "public"
  }
}
```

### Planned Response

```json
{
  "query": "What is the refund policy?",
  "strategy": "hybrid_dense_bm25_rrf_v1",
  "top_k": 5,
  "results": [
    {
      "chunk_id": "chunk-id",
      "text": "matched chunk text",
      "fused_score": 0.92,
      "dense_score": 0.84,
      "sparse_score": 0.76,
      "metadata": {}
    }
  ]
}
```

### Acceptance Criteria

* Dense retrieval still works
* Sparse retrieval works
* Hybrid retrieval works
* RRF fusion returns ranked results
* Results show enough metadata to debug ranking
* Retrieval strategy is visible in response

## Phase 1D: DeepSeek Grounded Answer Generation

Status: Planned

### Goal

Generate answers only from retrieved context.

### Planned Items

* Create LLM provider interface
* Create DeepSeek adapter
* Add OpenAI-compatible client
* Add normalized chat request schema
* Add normalized chat response schema
* Add grounded answer prompt
* Add prompt versioning
* Add structured output contract
* Add context budgeting
* Add refusal behavior
* Add `/v1/ask`

### Planned API

```text
POST /v1/ask
```

### Acceptance Criteria

* User can ask a question
* System retrieves context
* DeepSeek generates answer from context
* Response follows structured schema
* System refuses when context is insufficient
* Prompt version is returned
* Model name is returned

## Phase 1E: Citation-Aware Answers

Status: Planned

### Goal

Return answers with exact source citations linked to chunks.

### Planned Items

* Add citation schema
* Add answer schema
* Add claim-to-chunk mapping
* Add citation rendering
* Add source URI in citation response
* Add chunk index in citation response
* Add document title in citation response

### Acceptance Criteria

* Every factual answer includes citations
* Citations include chunk IDs
* Citations include document title and source URI
* User can inspect the source chunk

## Phase 1F: Citation Verification and Confidence Scoring

Status: Planned

### Goal

Detect unsupported claims and score answer confidence.

### Planned Items

* Claim extraction
* Citation support check
* Lexical support baseline
* DeepSeek judge for ambiguous support checks
* Contradiction detection
* Confidence score
* Unsupported claim list
* Refusal reason

### Acceptance Criteria

* Unsupported claims are detected
* Citation support verdict is returned
* Confidence score is returned
* No-answer behavior works for missing information

## Phase 1G: Evaluation Suite

Status: Planned

### Goal

Add objective quality measurement.

### Planned Items

* Create golden eval set
* Add simple lookup questions
* Add multi-hop questions
* Add conflicting document questions
* Add stale document questions
* Add ambiguous questions
* Add no-answer questions
* Track retrieval recall@k
* Track MRR
* Track citation precision
* Track answer correctness
* Track refusal accuracy
* Generate Markdown or HTML eval report

### Acceptance Criteria

* At least 100 eval cases eventually
* Eval command can run locally
* Report is generated
* Retrieval and generation metrics are visible
* Regression thresholds can fail CI later

## Phase 1H: Observability and Tracing

Status: Planned

### Goal

Make every workflow debuggable.

### Planned Items

* Add trace ID generation
* Add request ID middleware
* Add structured logging
* Add retrieval trace
* Add prompt trace
* Add model call trace
* Add citation verification trace
* Add latency tracking
* Add error type tracking

### Acceptance Criteria

* Every answer has a trace ID
* Retrieval steps are traceable
* LLM calls are traceable
* Failed requests are traceable
* Latency per step is visible

## Phase 2: Evaluation-as-a-Service Platform

Status: Planned

### Goal

Build reusable internal eval service for RAG, summarization, extraction, and agents.

### Planned Items

* Dataset versioning
* Rubric versioning
* Judge config versioning
* DeepSeek judge prompts
* Human calibration set
* Batch eval jobs
* Eval reports
* Release gates

## Phase 3: AI Trace Explorer

Status: Planned

### Goal

Build trace explorer for LLM workflows.

### Planned Items

* Trace collector
* Span schema
* LLM call events
* Retrieval events
* Tool call events
* Waterfall UI
* Failure classification
* Eval-to-trace linking

## Phase 4: Permissioned Tool-Using Agent Sandbox

Status: Planned

### Goal

Build safe agent runtime where model proposes actions but deterministic code controls execution.

### Planned Items

* Tool registry
* Pydantic tool schemas
* RBAC
* Risk scoring
* Approval workflow
* Audit logs
* Agent traces
* Tool-use evals

## Phase 5: Fine-Tune vs RAG Decision Lab

Status: Planned

### Goal

Compare prompt-only, RAG, and LoRA fine-tuning with evidence.

### Planned Items

* Dataset builder
* Prompt-only baseline
* RAG variant
* LoRA/QLoRA variant
* Shared benchmark
* MLflow tracking
* Decision memo
* Model cards
* Dataset cards

## Immediate Next Step

Implement Phase 1C.

Recommended next commit:

```text
Add BM25 sparse retrieval and RRF hybrid fusion
```
