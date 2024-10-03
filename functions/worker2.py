def process_user_query(user_query):

    # Import
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
    from functions import llm
    from langchain_chroma import Chroma
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_community.document_loaders import WebBaseLoader
    from langchain.chains import RetrievalQA
    from langchain_openai import ChatOpenAI
    from langchain_openai import OpenAIEmbeddings
    from langchain.prompts import PromptTemplate
    import os
    from dotenv import load_dotenv
    from openai import OpenAI
    import streamlit as st  

    # Load Key
    if load_dotenv('.env'):
        OPENAI_KEY = os.getenv('OPENAI_API_KEY')
    else:
        OPENAI_KEY = st.secrets['OPENAI_API_KEY']

    # Pass the API Key to the OpenAI Client
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


    # Document Loading
    loader = WebBaseLoader(["https://www.cpf.gov.sg/member/retirement-income/government-support/silver-support-scheme","https://www.cpf.gov.sg/member/retirement-income"])
    docs = loader.load()

    # Document Splitting
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50, length_function=llm.count_tokens)
    splitted_documents = text_splitter.split_documents(docs)

    # Put into Vector Store
    embeddings_model = OpenAIEmbeddings(model='text-embedding-3-small')
    vector_store = Chroma.from_documents(
        collection_name="silver",
        documents=splitted_documents,
        embedding=embeddings_model,
        persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not neccesary
    )

    # Build Prompt
    template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Be as consise as possible. Always say "thanks for asking!" at the end of the answer.
    {context}
    Question: {question}
    Helpful Answer:"""
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    # Run Chain
    qa_chain = RetrievalQA.from_chain_type(
        ChatOpenAI(model='gpt-4o-mini'),
        retriever=vector_store.as_retriever(),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    response = qa_chain.invoke(user_query)
    return response["result"]