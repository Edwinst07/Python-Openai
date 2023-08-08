import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def analyze_feelings(text):
    prompt = f"Por favor, analiza el sentimiento predominante en el siguiente texto: '{text}'. el sentimiento es:"
    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        n=1,
        max_tokens = 100,
        temperature = 0.5
    )
    return response.choices[0].text.strip()

text = input("Ingresar texto: ")
feelings = analyze_feelings(text);
print(feelings)