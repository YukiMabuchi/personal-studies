import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_openai import OpenAIEmbeddings

from langchain.text_splitter import SpacyTextSplitter
from langchain_community.vectorstores import Chroma


load_dotenv()
pwd = os.path.dirname(os.path.abspath(__file__))

loader = PyMuPDFLoader(f"{pwd}/pdf/sample.pdf")
docs = loader.load()

text_splitter = SpacyTextSplitter(
    chunk_size=200,
    pipeline="ja_core_news_sm"
)
splitted_docs = text_splitter.split_documents(documents=docs)

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

db = Chroma(
    persist_directory=f"{pwd}/data",
    embedding_function=embeddings
)

db.add_documents(splitted_docs)

print("done")