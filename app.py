from dotenv import load_dotenv
import os
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA
from langchain import hub

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def process_url(url):
    loader = WebBaseLoader(url)
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(data)
    vector = FAISS.from_documents(documents, OpenAIEmbeddings())
    return vector

def process_user_input(vector, user_input):
    llm = ChatOpenAI(model="gpt-4o")
    prompt = hub.pull("rlm/rag-prompt")
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vector.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )
    result = qa_chain({"query": user_input})
    return result['result']

# Initialize session state for storing the vectors
if 'vectors' not in st.session_state:
    st.session_state.vectors = None

# UI for URL input
url = st.text_input("Enter Your URL")

if url and st.button('Submit URL'):
    st.session_state.vectors = process_url(url)
    st.success("URL processed successfully. You can now ask your question.")

# UI for question input
if st.session_state.vectors:
    user_input = st.text_input("Enter your question")
    if user_input and st.button('Submit Question'):
        result = process_user_input(st.session_state.vectors, user_input)
        st.write(result)
