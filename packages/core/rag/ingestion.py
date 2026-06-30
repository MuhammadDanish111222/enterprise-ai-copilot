from packages.core.rag.chunking import chunk_document
from packages.core.rag.loaders import load_text_document_from_bytes
from packages.schemas.documents import IngestionResult


def ingest_document_from_bytes(
    *,
    filename: str,
    content: bytes,
    source_uri: str | None = None,
) -> IngestionResult:
    document = load_text_document_from_bytes(
        filename=filename,
        content=content,
        source_uri=source_uri,
    )

    chunks = chunk_document(document)

    return IngestionResult(
        document=document,
        chunks=chunks,
        chunk_count=len(chunks),
    )