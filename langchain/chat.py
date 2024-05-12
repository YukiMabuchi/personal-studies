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
from langchain_core.runnables import RunnableParallel

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

"""
LCEL Runnable protocol
https://python.langchain.com/v0.1/docs/expression_language/

The Runnable executes the pipeline of operations calling invoke method on each
それぞれのクラスの中にinvoke methodがある、それを次々につぎつぎに呼び出している

RunnablePassthrough
https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.passthrough.RunnablePassthrough.html
originalのinputを保持する
"""
rag_chain_from_docs = (
    RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])))
    | custom_rag_prompt
    | llm
    | StrOutputParser()
)

"""
RunnableParallel
https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.base.RunnableParallel.html
It invokes Runnables concurrently, providing the same input to each.
Streamとかに使えそう
"""
rag_chain_with_source = RunnableParallel(
    {"context": retriever, "q": RunnablePassthrough()}
).assign(answer=rag_chain_from_docs)

res = rag_chain_with_source.invoke(q)

output = f"""Question: {res.get('q')}
Answer: {res.get('answer')}
Reference: {", ".join(list(set([r and r.metadata and r.metadata.get("file_path") or '' for r in res.get('context', [])])))}
"""

print(output)