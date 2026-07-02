from packages.core.rag.hashing import sha256_text, stable_uuid
from packages.schemas.documents import DocumentChunk, IngestedDocument


CHUNKER_NAME = "fixed_word_overlap_chunker"
CHUNKER_VERSION = "v1"


def estimate_tokens(text: str) -> int:
    return max(1, len(text.split()))


def chunk_document(
    document: IngestedDocument,
    *,
    max_words: int = 220,
    overlap_words: int = 40,
) -> list[DocumentChunk]:
    if overlap_words >= max_words:
        raise ValueError("overlap_words must be smaller than max_words.")

    words = document.content.split()

    if not words:
        return []

    chunks: list[DocumentChunk] = []
    start = 0
    chunk_index = 0

    while start < len(words):
        end = min(start + max_words, len(words))
        chunk_text = " ".join(words[start:end])
        chunk_hash = sha256_text(chunk_text)

        chunks.append(
            DocumentChunk(
                chunk_id=stable_uuid(
                    document.document_id,
                    CHUNKER_NAME,
                    CHUNKER_VERSION,
                    str(chunk_index),
                    chunk_hash,
                ),
                document_id=document.document_id,
                document_title=document.title,
                source_uri=document.source_uri,
                chunk_index=chunk_index,
                chunk_text=chunk_text,
                chunk_hash=chunk_hash,
                chunker=CHUNKER_NAME,
                chunker_version=CHUNKER_VERSION,
                token_count_estimate=estimate_tokens(chunk_text),
                metadata={
                    **document.metadata,
                    "doc_type": document.doc_type,
                    "access_level": document.access_level,
                    "document_hash": document.content_hash,
                    "start_word": start,
                    "end_word": end,
                },
            )
        )

        chunk_index += 1

        if end >= len(words):
            break

        start = end - overlap_words

    return chunks