# linear_regression.py

import numpy as np
from sklearn.linear_model import LinearRegression

def train_model():
    # Sample dataset
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_value(model, value):
    prediction = model.predict([[value]])
    return prediction[0]
