import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()
pwd = os.path.dirname(os.path.abspath(__file__))

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

db = Chroma(
    persist_directory=f"{pwd}/data",
    embedding_function=embeddings
)

q = "飛行車の最高速度は？"

docs = db.similarity_search(q)

doc_str = ""
for doc in docs:
    doc_str += f"""
-------------------
{doc.page_content}
"""

prompt = PromptTemplate(
    template=f"""文章を元に質問に答えてください。

文章:
{doc_str}

質問: {q}
""",
input_variables=["doc_str", "q"]
)

chat = ChatOpenAI(
    openai_api_key=os.getenv('OPENAI_API_KEY'),
    model="gpt-3.5-turbo-0125",
)

result = chat([
    HumanMessage(content=prompt.format(doc_str=doc_str, q=q))
])

print(result.content)