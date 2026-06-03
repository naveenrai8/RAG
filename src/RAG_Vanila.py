from core.llms import LLMProviders
from core.pdf_readers import PdfReader, PdfReaderTypes
from core.vector_store import FaissVectorStore, VectorStoreTypes
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from uuid import uuid4
import langchain
from core.data_loader import DataLoaderConfig, DataLoader

class VanilaRAG:
    def __init__(self, cfg: DataLoaderConfig):
        langchain.debug = True
        data_loader = DataLoader(cfg=cfg)
        self.llm = LLMProviders().azure_openai_llm()
        self.vs = data_loader.invoke()
    
    def invoke(self, query: str):
        
        similar_docs = self.vs.similarity_search(query=query, k=2)
        for sd in similar_docs:
            print(sd.page_content)
            print()
        
        messages = [
        (
            "system",
            f"Provide the answer of user's query from the attached docs {similar_docs}. If answer not found in the doc, return I don't know.",
        ),
        ("human", f"{query}"),
        ];

        response = self.llm.invoke(messages, {"query": query, "docs": similar_docs[0].page_content})
        print(response)
        print(response.content)

cfg = DataLoaderConfig(
    pdf_reader=PdfReaderTypes.PY_MU_PDF,
    file_name="HTTP-Status-Codes.pdf",
    chunk_size=50,
    chunk_overlap=200,
    vector_store=VectorStoreTypes.VS_FAISS
)
v_rag = VanilaRAG(cfg=cfg)
v_rag.invoke(query="what is error code 404")
