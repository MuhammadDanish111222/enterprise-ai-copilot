from typing import Any

from pydantic import BaseModel, Field

from packages.schemas.vector_store import VectorSearchResult


class SearchRequest(BaseModel):
    query: str = Field(min_length=1)
    top_k: int = Field(default=5, ge=1, le=20)
    filters: dict[str, Any] | None = None


class SearchResponse(BaseModel):
    query: str
    top_k: int
    results: list[VectorSearchResult]
    embedding_model: str
    vector_collection: str