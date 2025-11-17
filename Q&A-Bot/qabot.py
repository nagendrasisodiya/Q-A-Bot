import os
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from dotenv import load_dotenv
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_ibm import WatsonxLLM, WatsonxEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import gradio as gr

# Initializing our model
def get_llm():
    load_dotenv()
    api_key = os.getenv("WATSONX_API_KEY")
    print("Loaded API key:", api_key is not None)

    model_id = 'ibm/granite-3-3-8b-instruct'
    parameters = {
        GenParams.MAX_NEW_TOKENS: 256,
        GenParams.TEMPERATURE: 0.5,
    }
    project_id = "1a2c896a-daa8-4e13-865b-ef128168acde"
    watsonx_llm = WatsonxLLM(
        model_id=model_id,
        url="https://eu-de.ml.cloud.ibm.com",
        project_id=project_id,
        api_key=api_key,
        params=parameters
    )
    return watsonx_llm

# loading document
def document_loader(file):
    loader=PyPDFLoader(file.name)
    loaded_document=loader.load()
    return loaded_document


# splitting loaded a document into chunks
def text_splitor(data):
    text_splitor=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks=text_splitor.split_documents(data)
    return chunks

## Embedding model
def watsonx_embedding():
    watsonx_embedding = WatsonxEmbeddings(
        model_id="sentence-transformers/all-minilm-l6-v2",  # CORRECTED: Valid model
        url="https://eu-de.ml.cloud.ibm.com",
        project_id="1a2c896a-daa8-4e13-865b-ef128168acde",
        api_key=os.getenv("WATSONX_API_KEY")
    )
    return watsonx_embedding

# vector db
def vector_database(chunks):
    embeding_model=watsonx_embedding()
    vector_db=Chroma.from_documents(documents=chunks, embedding=embeding_model)
    return vector_db

# retriever
def retriever(file):
    splits=document_loader(file)
    chunks=text_splitor(splits)
    vector_db=vector_database(chunks)
    retriever=vector_db.as_retriever()
    return retriever

def qabot_retriever(file, query):
    llm=get_llm()
    retriever_obj=retriever(file)
    qa=RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever_obj, return_source_documents=True)
    response=qa(query)
    return response["result"]


gradio_interface=gr.Interface(
    fn=qabot_retriever,
    inputs=[gr.File(label="Upload your PDF file", file_count="single", file_types=[".pdf"], type="filepath"),
            gr.Textbox(label="Ask your question", lines=2, placeholder="Ask your question here")
            ],
    outputs=gr.Textbox(label="Answer"),
    title="Q&A Bot",
    description="Upload a PDF Document and ask questions to Q&A Bot"
)

gradio_interface.launch(server_name="127.0.0.1", server_port=8080)

