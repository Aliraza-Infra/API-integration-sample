# Architecture

- core/api_client.py: a thin requests wrapper with session handling and basic error logging.
- core/auth.py: token holder; extend this to implement refresh flows for OAuth2.
- integrations/: examples showing how to adapt the client for specific providers (GitHub, OpenAI).
- utils/logger.py: centralized logging setup for consistent logs.
- examples/: runnable scripts demonstrating integration usage.
