from agents.base_agent import BaseAgent
from llm_client import LLMClient

class FeedbackAgent(BaseAgent):
    def __init__(self):
        super().__init__("Feedback")
        self.llm = LLMClient()

    def run(self, data: dict) -> dict:
        draft_answer = data.get("draft_answer", "")
        evaluation = data.get("evaluation", {})

        prompt = f"""
        You are a feedback agent.

        Original Answer:
        {draft_answer}

        Evaluation:
        Correctness: {evaluation.get('correctness')}
        Missing Points: {evaluation.get('missing_points')}
        Issues: {evaluation.get('issues')}

        Improve the answer by:
        - Adding missing points
        - Fixing issues
        - Improving clarity
        """

        improved_answer = self.llm.generate(prompt)

        return {
            "agent": self.name,
            "output": improved_answer
        }
