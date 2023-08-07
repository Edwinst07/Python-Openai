import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

question_previous = []
response_previous = []

def question_chat_GTP(prompt, model="text-davinci-002"):
    response = openai.Completion.create(
        engine = model,
        prompt = prompt,
        n = 1,
        max_tokens = 150,
        temperature = 1.5
    )
    return response.choices[0].text.strip()

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
    print(f"{response_gpt}")
    
    question_previous.append(income_user)
    response_previous.append(response_gpt)
