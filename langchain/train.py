"""
https://python.langchain.com/v0.1/docs/use_cases/question_answering/quickstart/
"""
import os
from dotenv import load_dotenv
import shutil

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader # https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/pdf/

load_dotenv()
pwd = os.path.dirname(os.path.abspath(__file__))

# first rm all the trained data
# if it's ok to train data in in-memory, we don't need this
dir_path = f"{pwd}/tmp/data"
if os.path.exists(dir_path):
    shutil.rmtree(dir_path)
    os.makedirs(dir_path)

# training
loader = PyMuPDFLoader(f"{pwd}/src/pdf/attention_is_all_you_need.pdf") # attention_is_all_you_need.pdf
docs = loader.load()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)

vectorstore = Chroma(
    persist_directory=f"{pwd}/tmp/data",
    embedding_function=embeddings
)

splits = text_splitter.split_documents(docs)

vectorstore.add_documents(
    documents=splits,
    embedding=embeddings
)

print('training done')