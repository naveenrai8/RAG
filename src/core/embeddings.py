from langchain_core.embeddings import Embeddings
from config.settings import AzureSettings, EmbeddingModelConfig


def get_embedding_model(cfg: EmbeddingModelConfig) -> Embeddings:
    if cfg.embedding_provider == "azure_openai":

        from langchain_openai import AzureOpenAIEmbeddings

        s = AzureSettings()
        return AzureOpenAIEmbeddings(
            azure_deployment=s.azure_openai_embedding_deployment,
            azure_endpoint=s.azure_openai_endpoint,
            api_key=s.azure_openai_api_key,
            api_version=s.azure_openai_api_version,
        )
    raise ValueError(f"Unsupported embedding provider: {cfg.embedding_provider}")


cfg = EmbeddingModelConfig(embedding_provider="azure_openai", temperature=1.0)
llm = get_embedding_model(cfg)
print(llm.embed_query("Where is India"))
