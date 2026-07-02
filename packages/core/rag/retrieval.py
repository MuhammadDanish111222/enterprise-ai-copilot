from packages.core.config import get_settings
from packages.embedding_providers.sentence_transformers_provider import (
    SentenceTransformersEmbeddingProvider,
)
from packages.schemas.retrieval import SearchResponse
from packages.vector_stores.qdrant_store import QdrantVectorStore


class SemanticRetriever:
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

    def search(
        self,
        *,
        query: str,
        top_k: int = 5,
        filters: dict | None = None,
    ) -> SearchResponse:
        query_vector = self.embedding_provider.embed_texts([query])[0]

        results = self.vector_store.search(
            query_vector=query_vector,
            top_k=top_k,
            filters=filters,
        )

        return SearchResponse(
            query=query,
            top_k=top_k,
            results=results,
            embedding_model=self.embedding_provider.model_name,
            vector_collection=self.settings.qdrant_collection_name,
        )