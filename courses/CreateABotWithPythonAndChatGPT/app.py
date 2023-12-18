from openai import OpenAI, AuthenticationError, BadRequestError
import json
import httpx
import tiktoken
from open_ai_service import OpenAiService

enc = tiktoken.encoding_for_model('gpt-3.5-turbo')

# Requires secrets.json file in
secret_path = './secrets.json'

with open(secret_path) as f:
    data = json.load(f)

openai_service = OpenAiService(
    data['openai']['key'],
    'gpt-3.5-turbo'
)

openai_service.append_message({'role': 'system',
                               'content': 'you are a CTO mentoring developers, don\'t only provide answers, also ask guiding questions'})
openai_service.append_message({'role': 'user', 'content': 'Why is my website down?'})

tokens_for_prompt = openai_service.num_tokens_from_messages()
print('Tokens for prompt: ', tokens_for_prompt)
openai_service.get_completion()

input()
