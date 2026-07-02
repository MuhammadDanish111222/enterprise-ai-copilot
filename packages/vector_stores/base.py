from typing import Protocol

from packages.schemas.vector_store import VectorRecord, VectorSearchResult


class VectorStore(Protocol):
    def ensure_collection(self, *, vector_size: int) -> None:
        ...

    def upsert(self, *, records: list[VectorRecord]) -> None:
        ...

    def search(
        self,
        *,
        query_vector: list[float],
        top_k: int,
        filters: dict | None = None,
    ) -> list[VectorSearchResult]:
        ...