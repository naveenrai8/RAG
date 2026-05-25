from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
import faiss
from enum import Enum
from uuid import uuid4
from pathlib import Path
from core.root_path import get_project_root

class VectorStoreTypes(str, Enum):
    VS_FAISS = "faiss"

class FaissVectorStore:     
    def __init__(self):
        self.folder_path = get_project_root() / ".local_faiss_store"
    def load_embed_docs(self, embed_model, embed_dim, index_name, documents, ids) -> FAISS:
        
        if self._is_faiss_index_stored(folder_path=self.folder_path, index_name=index_name):
            print("🚀 Index found! Loading existing local FAISS vector store...")
            self.vs = FAISS.load_local(
                folder_path=self.folder_path,
                index_name=index_name,
                embeddings=embed_model, 
                allow_dangerous_deserialization=True)
        else:
            print("✨ Index not found. Generating new embeddings and creating local store...")
            self.vs = FAISS(
                embedding_function=embed_model,
                index=faiss.IndexFlatL2(embed_dim),
                docstore=InMemoryDocstore(),
                index_to_docstore_id={},
            )
            self._add_documents(documents=documents, ids=ids)
            self._save_on_disk(index_name=index_name)
        return self.vs

    def _add_documents(self, documents, ids = None):
        if not ids:
            ids = [str(uuid4) for _ in documents]
        self.vs.add_documents(documents=documents, ids= ids)
    
    def _save_on_disk(self, index_name):
        self.vs.save_local(
            folder_path=self.folder_path,
            index_name=index_name
        )

    def _is_faiss_index_stored(self, folder_path: str, index_name: str = "index") -> bool:
        """
        Checks if a local FAISS index exists at the specified directory.
        Looks for the core binary file (index_name.faiss).
        """
        dir_path = Path(folder_path)
        faiss_file = dir_path / f"{index_name}.faiss"
        
        # Returns True only if the directory exists and contains the .faiss file
        return dir_path.is_dir() and faiss_file.is_file()