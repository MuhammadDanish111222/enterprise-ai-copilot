import hashlib
import uuid


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def stable_uuid(*parts: str) -> str:
    raw = "::".join(parts)
    return str(uuid.uuid5(uuid.NAMESPACE_URL, raw))