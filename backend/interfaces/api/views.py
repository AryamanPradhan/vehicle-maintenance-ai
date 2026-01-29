from rest_framework.decorators import api_view
from rest_framework.response import Response

from domain.entities.vehicle import Vehicle
from domain.services.risk_assessment_service import RiskAssessmentService
from application.use_cases.predict_failure_use_case import PredictFailureUseCase
from infrastructure.ml.rule_based_predictor import RuleBasedPredictor
from infrastructure.genai.groq_llm_analyzer import GroqLLMAnalyzer

@api_view(["POST"])
def predict_failure(request):
    data = request.data
    vehicle = Vehicle(data["vehicle_id"], data["mileage"], data["usage_type"])

    use_case = PredictFailureUseCase(
        RuleBasedPredictor(),
        GroqLLMAnalyzer(),
        RiskAssessmentService()
    )
    return Response(use_case.execute(vehicle, data["complaint"]))
