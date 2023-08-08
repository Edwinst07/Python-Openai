import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def sortOut_text(text):
    categories = [
        "arte",
        "ciencia",
        "deporte",
        "economía",
        "educación",
        "entretenimiento",
        "medio ambiente",
        "politica",
        "salud",
        "tecnología"
    ]

    prompt = f"Por favor clasifica el siguiente texto '{text}' en una de estas categorías: {','.join(categories)}. La categoría es: "
    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        n = 1,
        max_tokens = 100,
        temperature = 0.6
    )
    return response.choices[0].text.strip()

text = input("ingrese el texto o articulo: ")
sortOut = sortOut_text(text)
print(sortOut)