# main.py

from linear_regression import train_model, predict_value

# Train model
model = train_model()

# Predict new value
value = 6
result = predict_value(model, value)

print("Input:", value)
print("Predicted Output:", result)
