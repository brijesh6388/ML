# KFold.py

import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error

# Create sample dataset
X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)

# Define model
model = LinearRegression()

# Define K-Fold
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

mse_scores = []

# Perform K-Fold Cross Validation
for train_index, test_index in kfold.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    mse_scores.append(mse)

print("MSE for each fold:", mse_scores)
print("Average MSE:", np.mean(mse_scores))
