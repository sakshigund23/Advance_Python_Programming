import numpy as np
import pandas as pd

# Create NumPy array of product prices
prices = np.array([50, 100, 80, 40, 120, 60])

# Calculate statistics
print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

# Create Pandas DataFrame
data = {
    "Product": ["Rice", "Sugar", "Oil", "Milk", "Biscuits", "Dal"],
    "Price": prices,
    "Quantity": [15, 8, 5, 12, 7, 20]
}

df = pd.DataFrame(data)

print("\nGrocery Store DataFrame:")
print(df)

# Display items having quantity less than 10
print("\nGrocery items having quantity less than 10:")
print(df[df["Quantity"] < 10])