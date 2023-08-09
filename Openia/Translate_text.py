import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def translate_text(text, language):
    prompt = f"Traduce el texto '{text}' al {language}."
    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = prompt,
        n=1,
        max_tokens = 200,
        temperature = 0.5
    )
    return response.choices[0].text.strip()

text = input("Ingrese el texto a traducir: ")
language = input("A qué idioma lo quiere traducir: ")
translate = translate_text(text, language)
print(translate)