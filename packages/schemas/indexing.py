from pydantic import BaseModel


class IndexingResult(BaseModel):
    document_id: str
    title: str
    source_uri: str
    chunk_count: int
    indexed_chunk_ids: list[str]
    embedding_model: str
    vector_collection: str