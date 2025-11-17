from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials
from langchain_ibm import WatsonxLLM

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
    params=parameters,
    apikey=
)

query=input("Enter your query testing query: ")
response=watsonx_llm.invoke(query)
print(response)