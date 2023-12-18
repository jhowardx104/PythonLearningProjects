import tiktoken
import httpx
from openai import OpenAI, AuthenticationError, BadRequestError


class OpenAiService:
    def __init__(self, api_key, model):
        self._api_key = api_key
        self._model = model
        self._messages = []
        self._openai_client = OpenAI(
            api_key=self._api_key,
            http_client=httpx.Client(
                verify=False
            )
        )

    def get_completion(self):
        try:
            response = self._openai_client.chat.completions.create(
                model=self._model,
                messages=self._messages
            )
            print('Raw response: \n', response)
            print('CTO response: \n', response.choices[0].message.content)
        except AuthenticationError:
            print("an error occurred authenticating with OpenAI")
        except BadRequestError:
            print("A malformed request was sent to OpenAI")

    def append_message(self, message):
        self._messages.append(message)

    def num_tokens_from_messages(self, model=''):
        if model == '':
            model = self._model

        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            print('Model not found. Using cl100k_base.')
            encoding = tiktoken.get_encoding('cl100k_base')
        if model in {
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-16k-0613",
            "gpt-4-0314",
            "gpt-4-32k-0314",
            "gpt-4-0613",
            "gpt-4-32k-0613"
        }:
            tokens_per_message = 3
            tokens_per_name = 1
        elif model == "gpt-3.5-turbo-0301":
            tokens_per_message = 4
            tokens_per_name = -1
        elif "gpt-3.5-turbo" in model:
            print('gpt-3.5-turbo detected. Defaulting to gpt-3.5-turbo-0613.')
            return self.num_tokens_from_messages(model='gpt-3.5-turbo-0613')
        elif "gpt-4" in model:
            print('gpt-4 detected. Defaulting to gpt-4-0613')
            return self.num_tokens_from_messages(model='gpt-4-0613')
        else:
            raise NotImplementedError(
                f"""num_tokens_from_messages() is not implemented for model {model}."""
            )
        num_tokens = 0
        for message in self._messages:
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(encoding.encode(value))
                if key == "name":
                    num_tokens += tokens_per_name
        num_tokens += 3
        return num_tokens
