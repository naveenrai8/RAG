from pathlib import Path

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class EmbeddingModelConfig(BaseModel):
    embedding_provider: str
    deployment: str | None = None
    model: str | None = None


class AzureSettings(BaseSettings):
    # read the env variable and ignore extra key=values in env file which aren't being referenced here.
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    azure_openai_api_key: str = ""
    azure_openai_endpoint: str = ""
    azure_openai_api_version: str = ""
    azure_openai_chat_deployment: str = ""
    azure_openai_embedding_deployment: str = ""


class LLMConfig(EmbeddingModelConfig):
    temperature: float = 0.0


class SplitterConfig(BaseModel):
    splitter_type: str = "recursive"
    chunk_size: int = 1000
    chunk_overlap: int = 150


class RetrieverConfig(BaseModel):
    k: int = 4
