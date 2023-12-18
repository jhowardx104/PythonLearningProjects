from openai import OpenAI
import json
import httpx

secret_path = '../../secrets.json'

with open(secret_path) as f:
    data = json.load(f)

openai_client = OpenAI(
    api_key=data['openai']['key'],
    # Skip verifying SSL Cert due to VPN issues
    http_client=httpx.Client(
        verify=False
    )
)

message = {'role': 'user', 'content': 'What is the oldest known dinosaur?'}
messages = [message]

response = openai_client.chat.completions.create(model='gpt-3.5-turbo', messages=messages)

print(response)

input()