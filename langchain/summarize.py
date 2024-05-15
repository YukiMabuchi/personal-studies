"""
https://python.langchain.com/v0.1/docs/use_cases/summarization/
"""

import os
from dotenv import load_dotenv

from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.combine_documents.map_reduce import MapReduceDocumentsChain
from langchain.chains.combine_documents.reduce import ReduceDocumentsChain
from langchain.chains.llm import LLMChain
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

pwd = os.path.dirname(os.path.abspath(__file__))
loader = PyMuPDFLoader(f"{pwd}/src/pdf/attention_is_all_you_need.pdf")
docs = loader.load()

llm = ChatOpenAI(
    temperature=0,
    model_name="gpt-3.5-turbo-0125",
    organization=os.getenv('ORG_ID'),
)


# Staff
# # Define prompt
# prompt_template = """Write an one sentence summary of the following in Japanese:

# "{text}"

# """
# prompt = PromptTemplate.from_template(prompt_template)

# # Define LLM chain
# llm_chain = LLMChain(llm=llm, prompt=prompt)

# # Define StuffDocumentsChain
# stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")
# summary = stuff_chain.run(docs)
# print(summary)

# Map reduce
# Define prompt
map_template = """The following is a set of documents
{docs}
Based on this list of docs, please identify the main themes 
Helpful Answer:"""
map_prompt = PromptTemplate.from_template(map_template)
map_chain = LLMChain(llm=llm, prompt=map_prompt)

# Reduce
reduce_template = """The following is set of summaries:
{docs}
Take these and distill it into a final, consolidated and one sentence summary of the main themes. 
Helpful Answer:"""
reduce_prompt = PromptTemplate.from_template(reduce_template)

# Run chain
reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)

# Takes a list of documents, combines them into a single string, and passes this to an LLMChain
combine_documents_chain = StuffDocumentsChain(
    llm_chain=reduce_chain, document_variable_name="docs"
)

# Combines and iteratively reduces the mapped documents
reduce_documents_chain = ReduceDocumentsChain(
    # This is final chain that is called.
    combine_documents_chain=combine_documents_chain,
    # If documents exceed context for `StuffDocumentsChain`
    collapse_documents_chain=combine_documents_chain,
    # The maximum number of tokens to group documents into.
    token_max=4000,
)

# Combining documents by mapping a chain over them, then combining results
map_reduce_chain = MapReduceDocumentsChain(
    # Map chain
    llm_chain=map_chain,
    # Reduce chain
    reduce_documents_chain=reduce_documents_chain,
    # The variable name in the llm_chain to put the documents in
    document_variable_name="docs",
    # Return the results of the map steps in the output
    return_intermediate_steps=False,
)

text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=1000, chunk_overlap=0
)
split_docs = text_splitter.split_documents(docs)

summary = map_reduce_chain.run(split_docs)
print(summary)