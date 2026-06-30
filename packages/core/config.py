from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_env: str = Field(default="local", alias="APP_ENV")
    app_name: str = Field(default="Enterprise AI Copilot", alias="APP_NAME")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    supabase_url: str | None = Field(default=None, alias="SUPABASE_URL")
    supabase_anon_key: str | None = Field(default=None, alias="SUPABASE_ANON_KEY")
    supabase_service_role_key: str | None = Field(
        default=None,
        alias="SUPABASE_SERVICE_ROLE_KEY",
    )

    database_url: str | None = Field(default=None, alias="DATABASE_URL")

    llm_provider: str = Field(default="deepseek", alias="LLM_PROVIDER")
    llm_base_url: str | None = Field(default=None, alias="LLM_BASE_URL")
    llm_chat_model: str | None = Field(default=None, alias="LLM_CHAT_MODEL")
    llm_reasoner_model: str | None = Field(default=None, alias="LLM_REASONER_MODEL")
    deepseek_api_key: str | None = Field(default=None, alias="DEEPSEEK_API_KEY")

    embedding_provider: str = Field(default="local_bge", alias="EMBEDDING_PROVIDER")
    embedding_model: str = Field(
        default="BAAI/bge-small-en-v1.5",
        alias="EMBEDDING_MODEL",
    )

    vector_store: str = Field(default="qdrant", alias="VECTOR_STORE")
    qdrant_url: str = Field(default="http://localhost:6333", alias="QDRANT_URL")

    trace_enabled: bool = Field(default=True, alias="TRACE_ENABLED")


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()