#This file was created by Aidan DeVera
#Sources in the README file


#Title: MyGPT
#Goals: 
'''
Using an llm(large language model) created from python 
Using pygame, create an interface for the chatbot 
'''

import openai
import pygame
import llm
from UI import*
 


model = llm.get_model("gpt-3.5-turbo")
model.key = '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'
response = model.prompt("What was the civil war?")
print(response.text())

 







