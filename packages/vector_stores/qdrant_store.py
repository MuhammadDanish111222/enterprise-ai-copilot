from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    FieldCondition,
    Filter,
    MatchValue,
    PointStruct,
    VectorParams,
)

from packages.schemas.vector_store import VectorRecord, VectorSearchResult


class QdrantVectorStore:
    def __init__(
        self,
        *,
        url: str,
        collection_name: str,
        api_key: str | None = None,
    ) -> None:
        self.client = QdrantClient(
            url=url,
            api_key=api_key,
        )
        self.collection_name = collection_name

    def ensure_collection(self, *, vector_size: int) -> None:
        try:
            self.client.get_collection(self.collection_name)
        except Exception:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE,
                ),
            )

    def upsert(self, *, records: list[VectorRecord]) -> None:
        if not records:
            return

        points = [
            PointStruct(
                id=record.id,
                vector=record.vector,
                payload={
                    "text": record.text,
                    **record.metadata,
                },
            )
            for record in records
        ]

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

    def search(
        self,
        *,
        query_vector: list[float],
        top_k: int,
        filters: dict | None = None,
    ) -> list[VectorSearchResult]:
        search_filter = self._build_filter(filters)

        response = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            query_filter=search_filter,
            limit=top_k,
        )

        results: list[VectorSearchResult] = []

        for point in response.points:
            payload = point.payload or {}
            text = str(payload.get("text", ""))

            metadata = {
                key: value
                for key, value in payload.items()
                if key != "text"
            }

            results.append(
                VectorSearchResult(
                    chunk_id=str(point.id),
                    score=float(point.score),
                    text=text,
                    metadata=metadata,
                )
            )

        return results

    def _build_filter(self, filters: dict | None) -> Filter | None:
        if not filters:
            return None

        return Filter(
            must=[
                FieldCondition(
                    key=key,
                    match=MatchValue(value=value),
                )
                for key, value in filters.items()
            ]
        )