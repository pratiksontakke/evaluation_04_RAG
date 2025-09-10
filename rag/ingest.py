from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_chroma.vectorstores import Chroma
from langchain_community.document_loaders.pdf import BasePDFLoader
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from rag.embedding_model import embeddings
loader = PyPDFLoader(file_path="./files/170603762v7.pdf")
documents = loader.load()

print(documents[0].page_content[:500])


text_splitter = RecursiveCharacterTextSplitter(, chunk_size=1000, chunk_overlap=250)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=200, 
    separators=["\n\n", "\n", " ", ""],
    add_start_index=True,
)
all_splits  = text_splitter.split_documents(documents)

# document_ids = vector_store.add_documents(documents=all_splits)


vector_store = Chroma(
                collection_name="foo",
                embedding_function=embeddings,
            )

vector_store.add_documents(documents=all_splits)
