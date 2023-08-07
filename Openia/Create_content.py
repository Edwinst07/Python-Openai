import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def create_content(issue, tokens, temperature, model="text-davinci-002"):
    prompt = f"por favor escribe un articulo corto sobre el tema: {issue}\n\n"
    response = openai.Completion.create(
        engine = model,
        prompt = prompt,
        n = 1,
        max_tokens = tokens,
        temperature = temperature
    )
    return response.choices[0].text.strip()

def resume_text(text, tokens, temperature, model="text-davinci-002"):
    prompt=f"por favor resume el siguiente texto en español: {text}\n\n"
    response=openai.Completion.create(
        engine=model,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperature
    )
    return response.choices[0].text.strip()

#issue = input("Ingrese el tema de tu articulo: ")
#tokens = int(input("Cuantos tokens tendra tu articulo: "))
#temperature = int(input("Del 1 al 10, que tan creativo quieres que sea tu articulo: "))/10
#article_created = create_content(issue, tokens, temperature)
#print(article_created)

origin = input("Pega aqui el articulo que quieres resumir (sin saltos de línea): ")
tokens = int(input("Cuántos tokens tendra tu articulo: "))
temperature = int(input("Del 1 al 10, qué tan creativo quieres que sea tu articulo: "))/10
resumen = resume_text(origin, tokens, temperature)
print(resumen)