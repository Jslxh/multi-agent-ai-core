import os

# Example: OpenAI-style client abstraction
# (We keep it generic – implementation can change later)

class LLMClient:
    def __init__(self):
        # Later you can load from env
        self.model_name = "gpt-4o-mini"  # placeholder

    def generate(self, prompt: str) -> str:
        """
        Sends prompt to LLM and returns response.
        Replace the internals with actual API call.
        """
        # TEMPORARY MOCK (for safe testing)
        return f"[LLM RESPONSE]\n{prompt}"
