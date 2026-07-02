from packages.core.config import get_settings
from packages.core.rag.ingestion import ingest_document_from_bytes
from packages.embedding_providers.sentence_transformers_provider import (
    SentenceTransformersEmbeddingProvider,
)
from packages.schemas.indexing import IndexingResult
from packages.schemas.vector_store import VectorRecord
from packages.vector_stores.qdrant_store import QdrantVectorStore


class DocumentIndexer:
    def __init__(self) -> None:
        self.settings = get_settings()

        self.embedding_provider = SentenceTransformersEmbeddingProvider(
            model_name=self.settings.embedding_model,
        )

        self.vector_store = QdrantVectorStore(
    url=self.settings.qdrant_url,
    collection_name=self.settings.qdrant_collection_name,
    api_key=self.settings.qdrant_api_key,
)

    def index_document_from_bytes(
        self,
        *,
        filename: str,
        content: bytes,
        source_uri: str | None = None,
        access_level: str = "public",
    ) -> IndexingResult:
        ingestion_result = ingest_document_from_bytes(
            filename=filename,
            content=content,
            source_uri=source_uri,
            access_level=access_level,
        )

        chunks = ingestion_result.chunks
        texts = [chunk.chunk_text for chunk in chunks]

        vectors = self.embedding_provider.embed_texts(texts)

        self.vector_store.ensure_collection(
            vector_size=self.embedding_provider.dimension,
        )

        records = [
            VectorRecord(
                id=chunk.chunk_id,
                text=chunk.chunk_text,
                vector=vector,
                metadata={
                    **chunk.metadata,
                    "chunk_id": chunk.chunk_id,
                    "document_id": chunk.document_id,
                    "document_title": chunk.document_title,
                    "source_uri": chunk.source_uri,
                    "chunk_index": chunk.chunk_index,
                    "chunk_hash": chunk.chunk_hash,
                    "chunker": chunk.chunker,
                    "chunker_version": chunk.chunker_version,
                    "token_count_estimate": chunk.token_count_estimate,
                    "embedding_model": self.embedding_provider.model_name,
                },
            )
            for chunk, vector in zip(chunks, vectors, strict=True)
        ]

        self.vector_store.upsert(records=records)

        return IndexingResult(
            document_id=ingestion_result.document.document_id,
            title=ingestion_result.document.title,
            source_uri=ingestion_result.document.source_uri,
            chunk_count=len(chunks),
            indexed_chunk_ids=[chunk.chunk_id for chunk in chunks],
            embedding_model=self.embedding_provider.model_name,
            vector_collection=self.settings.qdrant_collection_name,
        )