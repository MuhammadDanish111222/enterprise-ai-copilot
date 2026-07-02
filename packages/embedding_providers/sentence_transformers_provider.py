from functools import cached_property

from sentence_transformers import SentenceTransformer


class SentenceTransformersEmbeddingProvider:
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    @cached_property
    def model(self) -> SentenceTransformer:
        return SentenceTransformer(self.model_name)

    @cached_property
    def dimension(self) -> int:
        dimension = self.model.get_sentence_embedding_dimension()

        if dimension is None:
            raise RuntimeError("Could not detect embedding dimension.")

        return dimension

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )

        return embeddings.tolist()