from langchain_core.language_models import BaseChatModel

from config.settings import AzureSettings, LLMConfig
from logger import get_logger

log = get_logger(logger_name=f"{__file__}", print_on_stdio=False)

def get_llm(cfg: LLMConfig) -> BaseChatModel:
    if cfg.embedding_provider == "azure_openai":
        from langchain_openai import AzureChatOpenAI

        s = AzureSettings()
        log.info(s)
        return AzureChatOpenAI(
            azure_deployment=s.azure_openai_chat_deployment,
            azure_endpoint=s.azure_openai_endpoint,
            api_key=s.azure_openai_api_key,
            api_version=s.azure_openai_api_version,
            temperature=cfg.temperature
        )

cfg = LLMConfig(embedding_provider="azure_openai", temperature=1.0)
llm = get_llm(cfg)
print(llm.invoke("Where is India"))
