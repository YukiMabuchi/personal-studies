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

# every time remove the pretrained data first
# if it's ok to train data in in-memory, we don't need this
dir_path = f"{pwd}/tmp/data"
if os.path.exists(dir_path):
    shutil.rmtree(dir_path)
    os.makedirs(dir_path)

# training
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)
vectorstore = Chroma(
    persist_directory=f"{pwd}/tmp/data",
    embedding_function=embeddings
)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)

training_data_path = f"{pwd}/src/pdf"
file_names = [f for f in os.listdir(training_data_path) if os.path.isfile(os.path.join(training_data_path, f))]

for fn in file_names:
    loader = PyMuPDFLoader(f"{pwd}/src/pdf/{fn}")
    docs = loader.load()

    splits = text_splitter.split_documents(docs)

    vectorstore.add_documents(
        documents=splits,
        embedding=embeddings
    )

print('training done')