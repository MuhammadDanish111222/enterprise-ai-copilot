from fastapi import APIRouter, File, HTTPException, UploadFile

from packages.core.rag.indexing import DocumentIndexer
from packages.core.rag.ingestion import ingest_document_from_bytes
from packages.schemas.documents import IngestionResult
from packages.schemas.indexing import IndexingResult

router = APIRouter(prefix="/v1/ingest", tags=["ingestion"])


@router.post("/files/preview", response_model=IngestionResult)
async def preview_file(file: UploadFile = File(...)) -> IngestionResult:
    try:
        content = await file.read()

        return ingest_document_from_bytes(
            filename=file.filename or "uploaded.txt",
            content=content,
            source_uri=file.filename,
        )

    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/files", response_model=IndexingResult)
async def ingest_and_index_file(file: UploadFile = File(...)) -> IndexingResult:
    try:
        content = await file.read()

        indexer = DocumentIndexer()

        return indexer.index_document_from_bytes(
            filename=file.filename or "uploaded.txt",
            content=content,
            source_uri=file.filename,
        )

    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc