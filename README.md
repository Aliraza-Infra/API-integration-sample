# Universal API Integration Starter

Created this reusable starter repo for universal API integrations and automation.
Contains a generic API client for repo, auth helpers and example integrations (GitHub, OpenAI),logging utilities and runnable examples.

## Quick start

```bash
# unzip the repo (if you are using the ZIP)
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."
python examples/run_github_example.py
```

## Structure
- core/: reusable API client + auth helpers
- integrations/: example integrations (github, openai)
- utils/: logging + helpers
- examples/: runnable example scripts
- config/settings.example.json: placeholder config

## Notes
- Replace placeholder keys in `config/settings.example.json` or use environment variables.
- The GitHub example uses public endpoints and works without auth.
- The OpenAI example expects an environment variable `OPENAI_API_KEY` (or you can fill config).
