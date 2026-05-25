import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
Default_dic = 'Data'

def get_project_root():
    if "PROJECT_ROOT" in os.environ:
        return Path(os.environ["PROJECT_ROOT"])

    # fallback
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if (parent / "pyproject.toml").exists():
            return parent

    raise RuntimeError("Project root not found")

def get_documents_path():
    project_root = get_project_root()
    return project_root / os.getenv('RAG_DOCUMENT_DIR_NAME', Default_dic)