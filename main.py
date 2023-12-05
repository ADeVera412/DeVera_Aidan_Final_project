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


from openai import OpenAI
import pydantic
from pydantic import BaseModel
import os

client = OpenAI()
completion = client.completions.create(model='curie')
print(completion.choices[0].text)
print(dict(completion).get('usage'))
print(completion.model_dump_json(indent=2))
  #os.environ['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'],  # this is also the default, it can be omitted









