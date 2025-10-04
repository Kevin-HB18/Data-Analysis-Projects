# -*- coding: utf-8 -*-
import joblib
import pandas as pd

class ChurnPredictor:
    def __init__(self, pipeline, feature_names):
        # Cargar el modelo entrenado desde disco
        self.pipeline = pipeline
        self.feature_names = feature_names

    def predict(self, new_data):
        # Convertir dict → DataFrame
        if isinstance(new_data, dict):
            new_data = pd.DataFrame([new_data], columns=self.feature_names)

        pred = self.pipeline.predict(new_data)[0]
        proba = self.pipeline.predict_proba(new_data)[0,1]

        return {
            "prediction": int(pred),
            "probability_churn": round(proba, 3),
            "label": "Churn" if pred == 1 else "No Churn"
        }
