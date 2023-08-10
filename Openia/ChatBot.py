import openai
import os
import spacy
import numpy as np
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

question_previous = []
response_previous = []
model_spacy = spacy.load("es_core_news_md")
forbidden_words = ["madrid","palabra2"] # add forbidden words

def similarity_coseno(vec1, vec2):
    overlap = np.dot(vec1, vec2)
    magnitude1 = np.linalg.norm(vec1)
    magnitude2 = np.linalg.norm(vec2)
    sim_cos = overlap / (magnitude1 * magnitude2)
    return sim_cos

def es_relevant(response, entrance, umbral=0.5):
    entrance_vectorized = model_spacy(entrance).vector
    response_vectorized = model_spacy(response).vector
    similarity = similarity_coseno(entrance_vectorized, response_vectorized)
    return similarity >= umbral 

def filter_list_black(text, list_black):
    token =model_spacy(text)
    result =[]
    for t in token:
        if t.text.lower() not in list_black:
            result.append(t.text)
        else:
            result.append("[xxxx]")

    return " ".join(result)



def question_chat_GTP(prompt, model="text-davinci-002"):
    response = openai.Completion.create(
        engine = model,
        prompt = prompt,
        n = 1,
        max_tokens = 150,
        temperature = 1.5
    )
    response_uncontrolled = response.choices[0].text.strip()
    response_controlled = filter_list_black(response_uncontrolled, forbidden_words)
    return response_controlled

print("Bienvenido al chatBot basico. Escriba salir cuando quiera salir.")

while True:
    historical_Convesation = ""
    income_user = input("\nTú:")
    if income_user.lower() == "salir":
        break

    for question, response in zip(question_previous, response_previous):
        historical_Convesation += f"El usuario pregunta: {question}\n"
        historical_Convesation += f"ChatGPT responde: {response}\n"

    prompt = f"El usuario pregunta {income_user}\n"
    historical_Convesation += prompt
    response_gpt = question_chat_GTP(historical_Convesation) 

    relevant = es_relevant(response_gpt, income_user)

    if relevant:
        print(f"{response_gpt}")
        question_previous.append(income_user)
        response_previous.append(response_gpt)
    else:
        print("La respuesta no es relevante !!")
