from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from langchain.text_splitter import MarkdownTextSplitter
from langchain.text_splitter import PythonCodeTextSplitter
from langchain_experimental.text_splitter import SemanticChunker


class ChopDoc():
    def __init__(self):
        pass

    @staticmethod
    def character_splitter(text, chunk_size: int = 35, chunk_overlap: int = 0, separator: str = '', strip_whitespace: bool = True):
        text_splitter = CharacterTextSplitter(chunk_size=chunk_size,
                                              chunk_overlap=chunk_overlap,
                                              separator=separator,
                                              strip_whitespace=strip_whitespace)
        chunk_result = text_splitter.create_documents([text])
        return chunk_result

    @staticmethod
    def recursive_character_splitter(text, chunk_size: int = 35, chunk_overlap: int = 0, separator: str = '', strip_whitespace: bool = True):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                       chunk_overlap=chunk_overlap,
                                                       separators=separator,
                                                       strip_whitespace=strip_whitespace)
        chunk_result = text_splitter.create_documents([text])
        return chunk_result

    @staticmethod
    def document_specific_splitter(text, type: str, chunk_size: int = 35, chunk_overlap: int = 0):
        if type == 'markdown':
            text_splitter = MarkdownTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        elif type == 'python':
            text_splitter = PythonCodeTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        elif type == 'javascript':
            text_splitter = RecursiveCharacterTextSplitter.from_language(
                language=Language.JS, chunk_size=chunk_size, chunk_overlap=chunk_overlap
            )

        result = text_splitter.create_documents([text])
        return result

    @staticmethod
    def semantic_splitter(text, embedding_method):
        text_splitter = SemanticChunker(embedding_method)
        result = text_splitter.create_documents([text])
        return result