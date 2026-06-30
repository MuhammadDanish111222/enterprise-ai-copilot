from pathlib import Path

from packages.schemas.documents import IngestedDocument, DocumentType


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

    if not text.strip():
        raise ValueError("File content is empty.")

    return IngestedDocument(
        source_uri=source_uri or filename,
        title=Path(filename).stem,
        doc_type=SUPPORTED_EXTENSIONS[extension],
        content=text.strip(),
        metadata={
            "filename": filename,
            "extension": extension,
        },
    )