"""
https://python.langchain.com/v0.1/docs/use_cases/question_answering/quickstart/
"""

import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

pwd = os.path.dirname(os.path.abspath(__file__))

llm = ChatOpenAI(
    model="gpt-3.5-turbo-0125",
    organization=os.getenv('ORG_ID'),
)

q = 'Tell me about Transformer.'

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)
vectorstore = Chroma(
    persist_directory=f"{pwd}/tmp/data",
    embedding_function=embeddings
)

template = """Use the following pieces of context to answer the question at the end.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Use three sentences maximum and keep the answer as concise as possible.

{context}

Question: {q}

Helpful Answer:"""
custom_rag_prompt = PromptTemplate.from_template(template)

retriever = vectorstore.as_retriever(search_type="similarity")
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "q": RunnablePassthrough()}
    | custom_rag_prompt
    | llm
    | StrOutputParser()
)

res = rag_chain.invoke(q)

print(f"Result: {res}")