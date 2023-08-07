import os
import openai
import spacy
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

#models = openai.Model.list() 
#print(models)

model = "text-davinci-002"
prompt = "historia de un viaje a Europa"

response = openai.Completion.create(
    engine= model, 
    prompt= prompt,
    n=1,
    temperature=1,
    max_tokens = 50
)

for idx, option in enumerate(response.choices):
    text_generate = option.text.strip()
    print(f"Response {idx +1}: {text_generate}\n")

print("***")
model_spacy = spacy.load("es_core_news_md")

analysis = model_spacy(text_generate)

#for token in analysis:
 #   print(token.text, token.pos_)

#for ent in analysis.ents:
#    print(ent.text, ent.label)

location = None
for ent in analysis.ents:
    if ent.label == "LOC":
        location = ent
        break

if location:
    prompt2 = f"dime más a cerca de {location}"
    response2 = openai.Completion.create(
        engine= model,
        prompt = prompt2,
        n=1,
        max_tokens= 100
    )
    print(response2.choices[0].text.strip())
