from open_ai_service import OpenAiService
from secret_service import get_secrets

secrets = get_secrets()

# Construct OpenAI service using gpt-3.5-turbo
openai_service = OpenAiService(
    secrets['openai']['key'],
)

openai_service.append_sys_message('you are a CTO mentoring developers, don\'t only provide answers, also ask guiding questions')
openai_service.append_user_message('Why is my website down?')

tokens_for_prompt = openai_service.num_tokens_from_messages()
print('Tokens for prompt: ', tokens_for_prompt)
openai_service.get_completion()

input()
