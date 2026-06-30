# Project Roadmap

## Phase 0 - Foundation

Goal: Create clean project foundation.

- Project repo
- uv environment
- FastAPI base app
- Settings/config system
- Folder structure
- Documentation
- GitHub setup

## Phase 1 - Core RAG Copilot

Goal: Build the main AI product.

Features:
- Document upload
- Document parsing
- Chunking
- Embeddings
- Vector search
- Question answering
- Citations
- Basic refusal when context is missing

## Phase 2 - Verified Citations

Goal: Make answers trustworthy.

Features:
- Claim extraction
- Citation support checking
- Confidence score
- Unsupported claim detection
- No-answer behavior

## Phase 3 - Evaluation Module

Goal: Measure answer quality.

Features:
- Golden question set
- Retrieval accuracy
- Citation precision
- Answer correctness
- Regression reports

## Phase 4 - Trace / Observability Module

Goal: Debug every AI workflow.

Features:
- trace_id for each request
- LLM call logging
- Retrieval logs
- Prompt version tracking
- Latency tracking
- Error tracking

## Phase 5 - Permissioned Agent Module

Goal: Add safe tool-using AI actions.

Features:
- Tool registry
- Typed tool schemas
- Role checks
- Approval workflow
- Audit logs
- Safe execution

## Phase 6 - Fine-tune vs RAG Decision Lab

Goal: Compare architecture choices.

Features:
- Prompt-only baseline
- RAG comparison
- Fine-tuning comparison
- Cost/latency/quality report
- Architecture decision memo