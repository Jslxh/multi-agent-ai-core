from agents.base_agent import BaseAgent
from llm_client import LLMClient

class ExplainerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Explainer")
        self.llm = LLMClient()

    def run(self, data: dict) -> dict:
        query = data.get("query", "")
        plan = data.get("plan", [])

        prompt = f"""
        You are an explanation agent.

        Question:
        {query}

        Plan to follow:
        {plan}

        Write a clear, structured explanation following the plan.
        """

        explanation = self.llm.generate(prompt)

        return {
            "agent": self.name,
            "output": explanation
        }
