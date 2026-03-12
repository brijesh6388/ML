# dummy-variable.py

import pandas as pd

# Sample dataset
data = {
    "City": ["Delhi", "Mumbai", "Delhi", "Chennai", "Mumbai"],
    "Age": [25, 30, 35, 40, 28],
    "Salary": [50000, 60000, 65000, 70000, 62000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Create dummy variables
dummy = pd.get_dummies(df["City"])

# Combine with original dataset
df_new = pd.concat([df, dummy], axis=1)

# Drop original categorical column
df_new = df_new.drop("City", axis=1)

print("\nData after Dummy Variable Encoding:")
print(df_new)
