from langchain_text_splitters import RecursiveCharacterTextSplitter, TextSplitter

from config.settings import SplitterConfig


def get_splitter(cfg: SplitterConfig) -> TextSplitter:
    if cfg.splitter_type == "recursive":
        return RecursiveCharacterTextSplitter(
            chunk_size=cfg.chunk_size, chunk_overlap=cfg.chunk_overlap
        )
    raise ValueError(f"Unsupported Splitter type: {cfg.splitter_type}")
