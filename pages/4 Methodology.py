# Set up and run this Streamlit App
import streamlit as st

st.title("Methodology")

st.header("Implementation Details")

st.subheader("Retrieval Augmented Generation")
st.write("Both the Policy Explainer and Eligibility Checker utilise a simple RAG pipeline. Langchain WebBaseLoader is first used to load data from the relevant webpages, followed by RecursiveCharacterTextSplitter to split the document into chunks. Chroma database is used as vector store, with RetrievalQA used for retrieval. The prompt entered by the user (free-text for Policy Explainer and guided entry for Eligibility Checker) is then combined with a custom Q&A prompt to obtain output from LLM (gpt-4o-mini).")

st.subheader("Implementation Flowcharts")
st.write("The flowcharts for both the Policy Explainer and Eligibility Checker are attached below for reference")
st.image("flowchart.png", caption="Flowcharts for Policy Explainer (left) and Eligibility Checker (right).")
