from openai import OpenAI
import json
import httpx

# Requires secrets.json file in
secret_path = './secrets.json'

with open(secret_path) as f:
    data = json.load(f)

openai_client = OpenAI(
    api_key=data['openai']['key'],
    # Skip verifying SSL Cert due to VPN issues
    http_client=httpx.Client(
        verify=False
    )
)

messages = []
messages.append({'role': 'system', 'content': 'you are a CTO mentoring developers, don\'t only provide answers, also ask guiding questions'})
messages.append({'role': 'user', 'content': 'Why is my website down?'})

response = openai_client.chat.completions.create(model='gpt-3.5-turbo', messages=messages)

print(response.choices[0].message.content)

input()