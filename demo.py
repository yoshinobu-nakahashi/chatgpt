import os
import openai
import gradio as gr
from openai import ChatCompletion

# print(os.getenv('OPENAI_API_KEY')) 
openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
        {"role": "system", 
         "content": "You are a helpful assistant."},
        {"role": "user", 
         "content": "素数とはなんでしょうか"},
    ]
)

# レスポンスからメッセージ部分を抽出
for message in response['choices'][0]['message']['role']:
    print(f"{message['role']}: {message['content']}")