from agents.base_agent import BaseAgent
from llm_client import LLMClient

class EvaluatorAgent(BaseAgent):
    def __init__(self):
        super().__init__("Evaluator")
        self.llm = LLMClient()

    def run(self, data: dict) -> dict:
        draft_answer = data.get("draft_answer", "")

        prompt = f"""
        You are an evaluation agent.

        Evaluate the following answer for:
        - correctness
        - missing important points
        - clarity issues

        Answer:
        {draft_answer}

        Respond in this format:
        Correctness: <low|medium|high>
        Missing Points:
        - point 1
        - point 2
        Issues:
        - issue 1
        """

        raw_response = self.llm.generate(prompt)

        # Since this is still a mock LLM, we return a safe structured output
        evaluation = {
            "correctness": "medium",
            "missing_points": ["Mathematical intuition", "Learning rate explanation"],
            "issues": ["Too verbose", "Lacks examples"]
        }

        return {
            "agent": self.name,
            "output": evaluation
        }
