from pathlib import Path

from langchain_core.document_loaders import BaseLoader


def get_loader(path: str | Path) -> BaseLoader:
    p = Path(str)

    if p.suffix.lower() == ".pdf":
        from langchain_community.document_loaders import PyPDFLoader

        return PyPDFLoader(str(p))
    raise ValueError(f"Unsupported file type: {p.suffix}")
