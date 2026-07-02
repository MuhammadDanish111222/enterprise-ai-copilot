from typing import Any

from pydantic import BaseModel, Field


class VectorRecord(BaseModel):
    id: str
    text: str
    vector: list[float]
    metadata: dict[str, Any] = Field(default_factory=dict)


class VectorSearchResult(BaseModel):
    chunk_id: str
    score: float
    text: str
    metadata: dict[str, Any] = Field(default_factory=dict)