from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
import os
from dotenv import load_dotenv

class LLMProviders:
    def azure_openai_embedding(self, model = None):
        
        if not model:
            model = os.getenv("AZURE_OPENAI_EMBEDDING_LARGE_MODEL")
        api_version = os.getenv("AZURE_OPENAI_API_VERSION")

        embedding = AzureOpenAIEmbeddings( 
                api_version=api_version,
                azure_deployment=model,
        )

        dimension = len(embedding.embed_query('get dimension'))
        return embedding, dimension
        


    def azure_openai_llm(self, model = None) -> AzureChatOpenAI:
        if not model:
            model = os.getenv("AZURE_OPENAI_MODEL_GPT_5_NANO")
        api_version = os.getenv("AZURE_OPENAI_API_VERSION")

        return AzureChatOpenAI( 
                api_version=api_version,
                azure_deployment=model,
        )
