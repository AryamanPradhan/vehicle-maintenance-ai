from domain.interfaces.llm_analyzer import LLMAnalyzer

class GroqLLMAnalyzer(LLMAnalyzer):
    def extract_symptoms(self, text: str) -> dict:
        return {"vibration": "vibrate" in text.lower()}
