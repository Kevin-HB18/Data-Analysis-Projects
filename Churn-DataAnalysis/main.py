# -*- coding: utf-8 -*-
from churn_predictor import ChurnPredictor
import joblib

# Columnas originales
num_cols = ['Age', 'Tenure', 'Usage Frequency', 'Support Calls', 
            'Payment Delay', 'Last Interaction', 'Total Spend']
cat_cols = ['Gender', 'Subscription Type', 'Contract Length']
feature_names = num_cols + cat_cols

# Crear instancia cargando el modelo
xgb_clf = joblib.load("xgb_churn_model.pkl")
predictor = ChurnPredictor(xgb_clf, feature_names)
# Ejemplo de cliente
nuevo_cliente = {
    "Age": 19,
    "Tenure": 48,
    "Usage Frequency": 7,
    "Support Calls": 3,
    "Payment Delay": 30,
    "Last Interaction": 29,
    "Total Spend": 787.0,
    "Gender": "Female",
    "Subscription Type": "Premium",
    "Contract Length": "Annual"
}

nuevo_cliente2 = {
    "Age": 18,
    "Tenure": 12,
    "Usage Frequency": 3,
    "Support Calls": 2,
    "Payment Delay": 10,
    "Last Interaction": 5,
    "Total Spend": 525.8,
    "Gender": "Male",
    "Subscription Type": "Basic",
    "Contract Length": "Annual"
}

resultado = predictor.predict(nuevo_cliente)
resultado2 = predictor.predict(nuevo_cliente2)
print(resultado,resultado2)