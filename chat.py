# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 13:12:30 2023

@author: Christophe
"""

import random
import json
import re

import torch

from model import NeuralNet
from chatbot2 import bag_of_words, tokenize
from api_weather import meteo

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')



with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)
    

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Chrisbot"

def extract_city(question):
     pattern = r'in (.+?)\?'
     match = re.search(pattern, question)
     if match:
         city = match.group(1)
         return city
     else:
         return None
     
def get_response(msg,city):
    
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]
    print (tag)

   

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                if intent["tag"]== "meteo_temp":
                    JSON, JSON1 = meteo(city)
                    JSON1 = JSON1 - 273.15
                    # Utiliser les informations météo dans les réponses du fichier JSON
                    for response in intent['responses']:
                        if "{temperature}" in response:
                            response = response.replace("{temperature}", str(JSON1))
                        if "{description}" in response:
                            response = response.replace("{description}", JSON)
                        if "{city}" in response:
                            response = response.replace("{city}", city)
                        return response
                
                else:
                   return random.choice(intent['responses'])
    
    return "I do not understand..."


    
if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        # sentence = "do you use credit cards?"
        sentence = input("You: ")
        city=extract_city(sentence)
        print (city)
                        
        if sentence == "quit":
            break

        resp = get_response(sentence,city)
        print(resp)    




    
    