# Progress

## Current Project

Enterprise AI Copilot

## Current Focus

Project 1: Production RAG Copilot with Verified Citations

## Current Status

```text
Phase 0: Completed
Phase 1A: Completed
Phase 1B: Completed
Phase 1C: Next
```

## Latest Completed Phase

Phase 1B: Embeddings and Qdrant Semantic Retrieval

## Completed Work

### Phase 0: Foundation

Status: Completed

Completed:

* GitHub repository created
* Professional project structure created
* FastAPI app added
* `/health` endpoint added
* Shared config system added
* Environment variables planned
* `.env.example` added
* Core packages created
* Provider packages created
* Schema packages created
* Documentation added
* Roadmap added
* Architecture documentation added

### Phase 1A: Document Ingestion and Chunking

Status: Completed

Completed:

* Text file loader
* Markdown file loader
* UTF-8 validation
* Empty file validation
* Stable document ID generation
* Stable chunk ID generation
* Content hashing
* Chunk hashing
* Fixed word overlap chunker
* Chunker name stored
* Chunker version stored
* Token count estimate stored
* Metadata preserved
* Ingestion preview endpoint added

Endpoint added:

```text
POST /v1/ingest/files/preview
```

### Phase 1B: Embeddings and Qdrant Semantic Retrieval

Status: Completed

Completed:

* Sentence Transformers embedding provider
* Embedding provider interface
* BGE embedding model configured
* Qdrant vector store adapter
* Vector store interface
* Qdrant Docker Compose service
* Qdrant collection creation
* Chunk vector upsert
* Semantic retrieval service
* Ingest and index endpoint
* Semantic search endpoint

Endpoints added:

```text
POST /v1/ingest/files
POST /v1/retrieval/search
```

## Current Working Flow

```text
Upload file
-> Load document
-> Validate content
-> Create document hash
-> Create stable document ID
-> Split into chunks
-> Create chunk hashes
-> Create stable chunk IDs
-> Generate embeddings
-> Store vectors in Qdrant
-> Search chunks semantically
```

## Current API Endpoints

```text
GET /health
POST /v1/ingest/files/preview
POST /v1/ingest/files
POST /v1/retrieval/search
```

## Current Dependencies Added

```text
fastapi
uvicorn
pydantic
pydantic-settings
python-multipart
sentence-transformers
qdrant-client
numpy
```

## Current Docker Services

```text
qdrant
```

## Current Environment Variables

```text
APP_NAME
APP_ENV
EMBEDDING_MODEL
QDRANT_URL
QDRANT_COLLECTION_NAME
```

Planned:

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

## Current File Status

Important implemented files:

```text
apps/api/main.py
apps/api/routes/ingest.py
apps/api/routes/retrieval.py

packages/core/config.py
packages/core/rag/hashing.py
packages/core/rag/loaders.py
packages/core/rag/chunking.py
packages/core/rag/ingestion.py
packages/core/rag/indexing.py
packages/core/rag/retrieval.py

packages/embedding_providers/base.py
packages/embedding_providers/sentence_transformers_provider.py

packages/vector_stores/base.py
packages/vector_stores/qdrant_store.py

packages/schemas/documents.py
packages/schemas/indexing.py
packages/schemas/retrieval.py
packages/schemas/vector_store.py

docker-compose.yml
.env.example
README.md
docs/architecture.md
docs/roadmap.md
```

## Known Issues To Check

* Confirm `.env` is not tracked by Git
* Confirm `.gitignore` includes `.env`
* Confirm Qdrant starts with Docker Compose
* Confirm semantic search works after indexing a sample document
* Confirm README matches actual file names and endpoints
* Confirm old docs do not say the project is still only in documentation phase

## Next Phase

Phase 1C: Hybrid Retrieval with BM25 and RRF

## Phase 1C Tasks

Planned:

* Add sparse retrieval package
* Add BM25 dependency
* Create BM25 index from chunks
* Store sparse-searchable chunk records
* Add hybrid retrieval schema
* Add RRF fusion utility
* Add hybrid retrieval service
* Add hybrid retrieval endpoint
* Return dense, sparse, and fused scores
* Add retrieval strategy name
* Add tests for RRF ranking

## Next Commit Message

```text
Add BM25 sparse retrieval and RRF hybrid fusion
```

## Definition of Done for Phase 1C

Phase 1C is complete when:

* Dense search still works
* Sparse search works
* Hybrid search works
* RRF fusion combines both result lists
* Response includes ranking debug metadata
* Endpoint returns typed response
* Retrieval strategy is visible in the response
* Basic tests pass

## Long-Term Notes

Do not jump directly to DeepSeek answer generation before hybrid retrieval.

The correct next order is:

```text
1. BM25 sparse retrieval
2. RRF hybrid retrieval
3. DeepSeek adapter
4. Grounded answer generation
5. Citations
6. Citation verification
7. Evals
8. Traces
```
