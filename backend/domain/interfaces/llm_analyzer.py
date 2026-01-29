from abc import ABC, abstractmethod

class LLMAnalyzer(ABC):
    @abstractmethod
    def extract_symptoms(self, text: str) -> dict:
        pass
