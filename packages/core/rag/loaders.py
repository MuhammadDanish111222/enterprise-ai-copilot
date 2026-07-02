from pathlib import Path

from packages.core.rag.hashing import sha256_text, stable_uuid
from packages.schemas.documents import DocumentType, IngestedDocument


SUPPORTED_EXTENSIONS: dict[str, DocumentType] = {
    ".txt": "txt",
    ".md": "markdown",
    ".markdown": "markdown",
}


def load_text_document_from_bytes(
    *,
    filename: str,
    content: bytes,
    source_uri: str | None = None,
    access_level: str = "public",
) -> IngestedDocument:
    extension = Path(filename).suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {extension}. Supported: .txt, .md, .markdown"
        )

    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("File must be UTF-8 encoded text.") from exc

    text = text.strip()

    if not text:
        raise ValueError("File content is empty.")

    final_source_uri = source_uri or filename
    content_hash = sha256_text(text)

    return IngestedDocument(
        document_id=stable_uuid(final_source_uri, content_hash),
        source_uri=final_source_uri,
        title=Path(filename).stem,
        doc_type=SUPPORTED_EXTENSIONS[extension],
        content=text,
        content_hash=content_hash,
        access_level=access_level,
        metadata={
            "filename": filename,
            "extension": extension,
        },
    )