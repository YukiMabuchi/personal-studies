"""
https://python.langchain.com/v0.1/docs/use_cases/question_answering/quickstart/
"""
import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from langchain_core.prompts import PromptTemplate
from langchain.schema import HumanMessage

load_dotenv()

pwd = os.path.dirname(os.path.abspath(__file__))

llm = ChatOpenAI(
    model="gpt-3.5-turbo-0125",
)

q = 'Tell me about Transformer.'

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)
vectorstore = Chroma(
    persist_directory=f"{pwd}/tmp/data",
    embedding_function=embeddings
)
docs = vectorstore.similarity_search(q)

doc_str = ""
for doc in docs:
    print(f"doc: {doc.page_content}")
    doc_str += f"""
-------------------
{doc.page_content}
"""

template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Use three sentences maximum and keep the answer as concise as possible.

{context}

Question: {q}

Helpful Answer:"""

prompt = PromptTemplate(
    template=template,
    input_variables=['context', 'q']
)

result = llm([
    HumanMessage(content=prompt.format(context=doc_str, q=q))
])

print(result.content)