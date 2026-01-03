from agents.planner import PlannerAgent
from agents.explainer import ExplainerAgent
from agents.evaluator import EvaluatorAgent
from agents.feedback import FeedbackAgent

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.explainer = ExplainerAgent()
        self.evaluator = EvaluatorAgent()
        self.feedback = FeedbackAgent()

    def run(self, query: str) -> str:
        state = {"query": query}

        plan_result = self.planner.run(state)
        state["plan"] = plan_result["output"]

        explain_result = self.explainer.run(state)
        state["draft_answer"] = explain_result["output"]

        eval_result = self.evaluator.run(state)
        state["evaluation"] = eval_result["output"]

        feedback_result = self.feedback.run(state)

        return feedback_result["output"]
