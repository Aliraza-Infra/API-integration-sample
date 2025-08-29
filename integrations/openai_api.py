import os
from core.api_client import APIClient

class OpenAIApi:
    def __init__(self, api_key: str):
        headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
        self.client = APIClient('https://api.openai.com/v1', headers=headers)

    def simple_completion(self, prompt: str, model: str = 'gpt-3.5-turbo'):
        # Minimal example using Chat Completions endpoint structure
        payload = {
            'model': model,
            'messages': [{'role': 'user', 'content': prompt}],
            'max_tokens': 60
        }
        resp = self.client.post('/chat/completions', json=payload)
        return resp.json()
