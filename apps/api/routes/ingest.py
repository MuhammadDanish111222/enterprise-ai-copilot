from fastapi import APIRouter, File, HTTPException, UploadFile

from packages.core.rag.ingestion import ingest_document_from_bytes
from packages.schemas.documents import IngestionResult

router = APIRouter(prefix="/v1/ingest", tags=["ingestion"])


@router.post("/files", response_model=IngestionResult)
async def ingest_file(file: UploadFile = File(...)) -> IngestionResult:
    try:
        content = await file.read()

        return ingest_document_from_bytes(
            filename=file.filename or "uploaded.txt",
            content=content,
            source_uri=file.filename,
        )

    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc