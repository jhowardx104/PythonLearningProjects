import tiktoken

def num_tokens_from_messages(messages, model='gpt-3.5-turbo-0613'):
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
        return num_tokens_from_messages(messages, model='gpt-3.5-turbo-0613')
    elif "gpt-4" in model:
        print('gpt-4 detected. Defaulting to gpt-4-0613')
        return num_tokens_from_messages(messages, model='gpt-4-0613')
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3
    return num_tokens