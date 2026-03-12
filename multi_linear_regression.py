# multi_linear_regression.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    "area": [1000, 1500, 2000, 2500, 3000],
    "bedrooms": [2, 3, 3, 4, 4],
    "age": [10, 5, 8, 2, 1],
    "price": [200000, 300000, 350000, 450000, 500000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[["area", "bedrooms", "age"]]
y = df["price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict price
prediction = model.predict([[2200, 3, 5]])

print("Predicted House Price:", prediction[0])
