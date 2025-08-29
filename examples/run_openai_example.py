from utils.logger import setup_logging
from integrations.openai_api import OpenAIApi
import os

setup_logging()

def main():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print('OPENAI_API_KEY not set; skipping OpenAI demo.')
        return
    oa = OpenAIApi(api_key)
    res = oa.simple_completion('Say hello in one sentence.')
    print('OpenAI response (truncated):', str(res)[:400])

if __name__ == '__main__':
    main()
