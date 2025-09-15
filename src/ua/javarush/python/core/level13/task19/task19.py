# Using the OpenAI API
import os

# Write a program that uses the OpenAI API
# to get a response from the ChatGPT model.

### 🇺🇦 Ukrainian version:

# API від OpenAI

# Напишіть програму, яка використовує OpenAI API
# для отримання відповіді від моделі ChatGPT.

# Write your code here
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Tell me one fact about the Universe"}
    ],
    max_tokens=100
)

print(response.choices[0].message.content)
