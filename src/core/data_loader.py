from uuid import uuid4
from dataclasses import dataclass
from pathlib import Path
from langchain_community.vectorstores import FAISS
import faiss
from core.vector_store import FaissVectorStore, VectorStoreTypes
from core.llm_providers import LLMProviders
from core.pdf_readers import PdfReader, PdfReaderTypes



@dataclass
class DataLoaderConfig:
    pdf_reader: PdfReaderTypes
    file_name: str
    chunk_size: int
    chunk_overlap: int
    vector_store: VectorStoreTypes

    def index_name(self):
        file_name_without_ext = Path(self.file_name).stem
        return f"{file_name_without_ext}_{self.pdf_reader}_{self.chunk_size}_{self.chunk_overlap}_{self.vector_store}"

class DataLoader:
    def __init__(self, cfg: DataLoaderConfig):
        self.cfg = cfg
        self.index_name = cfg.index_name()
        

    def _load_pdf(self):
        pdf_reader = PdfReader()
        if (self.cfg.pdf_reader == PdfReaderTypes.PY_MU_PDF):
            documents = pdf_reader.pymupdf_reader(pdf_file_name=self.cfg.file_name)
        elif (self.cfg.pdf_reader == PdfReaderTypes.PY_PDF):
            documents = pdf_reader.pymupdf_reader(pdf_file_name=self.cfg.file_name)
        total_page = len(documents)
        for i, d in enumerate(documents):
            d.metadata = {**d.metadata, "Total": total_page, "Current": i}
        ids = [str(uuid4()) for _ in documents]
        return documents, ids
    

        
    def _create_embedding(self, vector_store: VectorStoreTypes, documents, ids) -> FAISS:
        if vector_store == VectorStoreTypes.VS_FAISS:
            llm_providers = LLMProviders()
            embed_provider, embed_dim = llm_providers.azure_openai_embedding()
            faiss_vs = FaissVectorStore()
            return faiss_vs.load_embed_docs(
                embed_dim=embed_dim,
                embed_model=embed_provider,
                index_name=self.index_name,
                documents=documents,
                ids=ids
            )
        else:
            print(f"No Vector store provided {vector_store}")
            
    
    def invoke(self):
        documents, ids = self._load_pdf()
        return self._create_embedding(self.cfg.vector_store, documents=documents, ids=ids)