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
import llm
from Data import*
 


model = llm.get_model("gpt-3.5-turbo")
model.key = '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'
#training_data 
response = model.prompt("What was the cold war?")
print(response.text())

 







