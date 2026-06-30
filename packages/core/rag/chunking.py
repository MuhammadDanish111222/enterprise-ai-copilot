from packages.schemas.documents import DocumentChunk, IngestedDocument


CHUNKER_NAME = "simple_paragraph_chunker_v1"


def estimate_tokens(text: str) -> int:
    return max(1, len(text.split()))


def chunk_document(
    document: IngestedDocument,
    *,
    max_words: int = 220,
    overlap_words: int = 40,
) -> list[DocumentChunk]:
    words = document.content.split()

    if not words:
        return []

    chunks: list[DocumentChunk] = []
    start = 0
    chunk_index = 0

    while start < len(words):
        end = min(start + max_words, len(words))
        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words)

        chunks.append(
            DocumentChunk(
                document_title=document.title,
                source_uri=document.source_uri,
                chunk_index=chunk_index,
                chunk_text=chunk_text,
                chunker=CHUNKER_NAME,
                token_count_estimate=estimate_tokens(chunk_text),
                metadata={
                    **document.metadata,
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