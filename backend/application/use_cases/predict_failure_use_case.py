class PredictFailureUseCase:
    def __init__(self, predictor, llm, risk_service):
        self.predictor = predictor
        self.llm = llm
        self.risk_service = risk_service

    def execute(self, vehicle, complaint):
        base_risk = self.predictor.predict(vehicle)
        symptoms = self.llm.extract_symptoms(complaint)
        final_risk = self.risk_service.assess(base_risk, symptoms)

        return {
            "vehicle_id": vehicle.vehicle_id,
            "failure_probability": final_risk,
            "recommendation": "Schedule inspection"
        }
