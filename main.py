#This file was created by Aidan DeVera
#Sources: https://platform.openai.com/docs/quickstart?context=python
#https://pypi.org/project/llm
#https://www.youtube.com/watch?v=q5HiD5PNuck




#Title: Star WarsGPT
#Goals: Have a working AI focused on Star Wars
'''
Using the OpenAI API, attempt to train the model on data from wookiepedia
'''

import openai

openai.api_key = "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"

messages = [ {"role":"system", "role":"You are a helpful assistant"} ]

while True:
  message = input("User: ")
  if message:
    messages.append(
      {"role": "user", "content": "message"}
    )
    chat = openai.Chatcompletion.create(
      model = "gpt-3.5-turbo", messages=messages, temperature=0.5
    )

  reply = chat.choices[0].message.content
  print(f"Chatgpt: {reply}")
  messages.append({"role": "assistant", "content": reply})











'''
def AI_bot(prompt):
    response = openai.Chatcompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
      user_input = input("You: ")
      if user_input.lower() in ["quit", "exit", "bye"]:
        break


response = AI_bot(user_input)
print("Chatbot: ", response)
'''





