from typing import Any, Literal

from pydantic import BaseModel, Field


DocumentType = Literal["txt", "markdown", "html", "pdf"]


class IngestedDocument(BaseModel):
    document_id: str
    source_uri: str
    title: str
    doc_type: DocumentType
    content: str
    content_hash: str
    access_level: str = "public"
    metadata: dict[str, Any] = Field(default_factory=dict)


class DocumentChunk(BaseModel):
    chunk_id: str
    document_id: str
    document_title: str
    source_uri: str
    chunk_index: int
    chunk_text: str
    chunk_hash: str
    chunker: str
    chunker_version: str
    token_count_estimate: int
    embedding_model: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class IngestionResult(BaseModel):
    document: IngestedDocument
    chunks: list[DocumentChunk]
    chunk_count: int