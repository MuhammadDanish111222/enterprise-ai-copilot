# Project Progress

## Current Status

Phase 0 foundation completed.

## Completed

### Phase 0 - Foundation

* [x] Created GitHub repository
* [x] Created local project folder
* [x] Initialized Git
* [x] Selected uv for Python environment management
* [x] Planned professional folder structure
* [x] Planned Supabase instead of local PostgreSQL
* [x] Planned FastAPI backend
* [x] Planned modular architecture
* [x] Created FastAPI app
* [x] Added `/health` endpoint
* [x] Added app settings/config system
* [x] Created professional folders
* [x] Added initial architecture and roadmap documentation

## Documentation Files Added

* [x] `PROJECT_CONTEXT.md`
* [x] `PROGRESS.md`
* [x] `ROADMAP.md`
* [x] `ARCHITECTURE.md`
* [x] `docs/decisions/ADR-0001-project-architecture.md`

## Current Step

Starting Phase 1: Core RAG Copilot.

## Next Step

Build the Core RAG Copilot foundation:

* Add document ingestion structure
* Add embedding provider interface
* Add vector storage plan using Supabase
* Add basic RAG pipeline
* Add API routes for document upload and chat
* Keep LLM provider replaceable
* Keep architecture modular and professional

## Decisions Made

* Use one single project, not five separate projects.
* Build RAG Copilot as the core.
* Add evals, tracing, agents, and decision lab as modules.
* Use Supabase managed PostgreSQL instead of local PostgreSQL.
* Use uv and `.venv` on Windows.
* Use DeepSeek first but keep LLM replaceable.
* Keep everything professional and modular.
* Use FastAPI as the backend framework.
* Use centralized app settings/config system.

## Blockers / Questions

None currently.
