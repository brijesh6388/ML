# logistic_regression.py

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Sample dataset
X = np.array([
    [22], [25], [47], [52], [46], [56], [48], [55], [60]
])  # Age

y = np.array([
    0, 0, 1, 1, 1, 1, 1, 1, 1
])  # Bought product (0 = No, 1 = Yes)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Predictions:", predictions)
print("Accuracy:", accuracy)
