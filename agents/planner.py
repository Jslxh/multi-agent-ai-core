from agents.base_agent import BaseAgent
from llm_client import LLMClient

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Planner")
        self.llm = LLMClient()

    def _clean_plan(self, raw_text: str) -> list:
        """
        Converts raw LLM text into a clean list of steps.
        """
        lines = raw_text.split("\n")

        steps = []
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Remove numbering if present
            if line[0].isdigit() and "." in line:
                line = line.split(".", 1)[1].strip()

            steps.append(line)

        return steps

    def run(self, data: dict) -> dict:
        query = data.get("query", "")

        prompt = f"""
        Break the following query into clear, logical steps.
        Return only the steps, one per line.

        Query: {query}
        """

        raw_response = self.llm.generate(prompt)
        plan = self._clean_plan(raw_response)

        return {
            "agent": self.name,
            "output": plan
        }
