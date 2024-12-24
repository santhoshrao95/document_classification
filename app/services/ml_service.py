import joblib
from pathlib import Path


class MLService:
    def __init__(self):
        model_path = Path("artifacts/models/random_forest_classifier_pipeline.joblib")
        self.pipeline = joblib.load(model_path)

    def predict(self, text: str):
        prediction = self.pipeline.predict([text])[0]
        prob = self.pipeline.predict_proba([text])[0].max()
        return prediction, prob
