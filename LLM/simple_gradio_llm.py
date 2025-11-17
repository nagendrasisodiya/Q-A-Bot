import os
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from langchain_ibm import WatsonxLLM
from dotenv import load_dotenv
import gradio as gr

load_dotenv()
api_key=os.getenv("WATSONX_API_KEY")

model_id='ibm/granite-3-3-8b-instruct'
parameters={
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE: 0.5,
}
project_id="1a2c896a-daa8-4e13-865b-ef128168acde"
watsonx_llm = WatsonxLLM(
     model_id=model_id,
     url="https://eu-de.ml.cloud.ibm.com",
     project_id=project_id,
     api_key=api_key,
     params=parameters
)

def genrate_response(query):
    response=watsonx_llm.invoke(query)
    return response

chat_interface=gr.Interface(
    fn=genrate_response,
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Enter your query here"),
    outputs=gr.Textbox(label="Output", lines=2, placeholder="Response will appear here"),
    title="Chat with Botbot",
    description="Ask questions to Chatbot",
)

chat_interface.launch(server_name="127.0.0.1", server_port=8080)