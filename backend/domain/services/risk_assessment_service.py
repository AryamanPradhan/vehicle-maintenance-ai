class RiskAssessmentService:
    def assess(self, base_risk: float, symptoms: dict) -> float:
        if symptoms.get("vibration"):
            base_risk += 0.2
        return min(base_risk, 1.0)
