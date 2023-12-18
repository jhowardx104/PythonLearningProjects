from openai import OpenAI, AuthenticationError, BadRequestError
import json
import httpx
import tiktoken
from open_ai_service import num_tokens_from_messages

enc = tiktoken.encoding_for_model('gpt-3.5-turbo')

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

tokens_for_prompt = num_tokens_from_messages(messages, model='gpt-3.5-turbo')

print('Tokens for prompt: ', tokens_for_prompt)

try:
    response = openai_client.chat.completions.create(model='gpt-3.5-turbo', messages=messages)
    print('Raw response: \n', response)
    print('CTO response: \n', response.choices[0].message.content)
except AuthenticationError:
    print("an error occurred authenticating with OpenAI")
except BadRequestError:
    print("A malformed request was sent to OpenAI")

input()