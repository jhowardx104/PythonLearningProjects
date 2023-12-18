import json

secret_path = './secrets.json'

with open(secret_path) as f:
    data = json.load(f)


def get_secrets():
    return data
