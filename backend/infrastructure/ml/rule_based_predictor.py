class RuleBasedPredictor:
    def predict(self, vehicle):
        return 0.6 if vehicle.mileage > 80000 else 0.3
