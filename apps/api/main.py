from fastapi import FastAPI
from apps.api.routes.ingest import router as ingest_router
from packages.core.config import get_settings

from apps.api.routes.ingest import router as ingest_router
from apps.api.routes.retrieval import router as retrieval_router

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Enterprise AI Copilot Platform API",
)

app.include_router(ingest_router)
app.include_router(retrieval_router)

@app.get("/health")
async def health_check() -> dict:
    return {
        "status": "ok",
        "app_name": settings.app_name,
        "environment": settings.app_env,
        "llm_provider": settings.llm_provider,
        "embedding_provider": settings.embedding_provider,
        "vector_store": settings.vector_store,
        "trace_enabled": settings.trace_enabled,
    }