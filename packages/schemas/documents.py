from typing import Literal
from pydantic import BaseModel, Field


DocumentType = Literal["txt", "markdown", "html", "pdf"]


class IngestedDocument(BaseModel):
    source_uri: str
    title: str
    doc_type: DocumentType
    content: str
    metadata: dict = Field(default_factory=dict)


class DocumentChunk(BaseModel):
    document_title: str
    source_uri: str
    chunk_index: int
    chunk_text: str
    chunker: str
    token_count_estimate: int
    metadata: dict = Field(default_factory=dict)


class IngestionResult(BaseModel):
    document: IngestedDocument
    chunks: list[DocumentChunk]
    chunk_count: int