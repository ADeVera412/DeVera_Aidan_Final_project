#This file was created by Aidan DeVera
#Sources: https://platform.openai.com/docs/quickstart?context=python
#https://pypi.org/project/llm
#https://www.youtube.com/watch?v=q5HiD5PNuck
#https://github.com/openai/openai-python/discussions/742



#Title: Star WarsGPT
#Goals: Have a working AI focused on Star Wars
'''
Using an llm(large language model) created from python, attempt to train the model on data from wookiepedia
'''

import openai
import pygame
import llm
from UI import*
 


model = llm.get_model("gpt-3.5-turbo")
model.key = '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'
response = model.prompt("What was the civil war?")
print(response.text())

 







