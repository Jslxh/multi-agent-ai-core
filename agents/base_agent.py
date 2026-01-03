from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def run(self, data: dict) -> dict:
        """
        Executes agent logic.
        Must return a dictionary with agent name and output.
        """
        pass
