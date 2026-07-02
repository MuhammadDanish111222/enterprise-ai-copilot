from fastapi import APIRouter

from packages.core.rag.retrieval import SemanticRetriever
from packages.schemas.retrieval import SearchRequest, SearchResponse

router = APIRouter(prefix="/v1/retrieval", tags=["retrieval"])


@router.post("/search", response_model=SearchResponse)
async def search_chunks(request: SearchRequest) -> SearchResponse:
    retriever = SemanticRetriever()

    return retriever.search(
        query=request.query,
        top_k=request.top_k,
        filters=request.filters,
    )