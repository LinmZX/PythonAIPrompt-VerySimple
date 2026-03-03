from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 2
numero_pessoas = 4
gosto_crianca = input("digite algo")

modelo_de_prompt = PromptTemplate(
    template="""
    Crie um roteiro de viagem de {dias} dias,
    para uma familia com {numero_criancas} criancas,
    que gostam de {atividade}
    """
)

prompt = modelo_de_prompt.format(
    dias=numero_dias,
    numero_criancas=numero_pessoas,
    atividade=gosto_crianca
)

print("Prompt : \n", prompt)


modelo = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.5,
    api_key=api_key
)

resposta = modelo.invoke(prompt)
print(resposta.content)