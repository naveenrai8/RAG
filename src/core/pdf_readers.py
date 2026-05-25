from typing import List, Iterator

from langchain_community.document_loaders import PyMuPDFLoader, PyPDFLoader
from enum import Enum
# from root_path import get_documents_path
from core.root_path import get_documents_path
from langchain_core.documents import Document

class PdfReaderTypes(str, Enum):
    PY_MU_PDF = "pymupdf",
    PY_PDF = "pypdf"

class PdfReader:
    def __init__(self):
        pass
            
    def pypdf_reader(self, pdf_file_name: str) -> List[Document]:
        file_path = get_documents_path() / pdf_file_name
        pdf_loader = PyPDFLoader(
            ile_path=file_path, 
            mode='page')
        return pdf_loader.load()

    def pymupdf_reader(self, pdf_file_name: str) -> List[Document]:
        file_path = get_documents_path() / pdf_file_name
        pymupdf_loader = PyMuPDFLoader(
            file_path=file_path
        )
        return pymupdf_loader.load()