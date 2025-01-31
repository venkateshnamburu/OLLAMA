import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"] = "GenAIAPPWithLangchain"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
       ("system","You are a helpful assistant. Please respond to the question asked"),
       ("user","question:{question}")        
    ]
)


## Streamlit Framework
st.title("Langchain Demo with LLAMA2")
input_text = st.text_input("What question you have in mind?")

## Ollama Llama2 Model
llm = Ollama(model="llama2",base_url = "http://127.0.0.1:11434")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
