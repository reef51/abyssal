import numpy as np

# Sales (Number of Cars Sold) and their respective probabilities
sales = np.array([0, 1, 2, 3, 4, 5])
probabilities = np.array([0.45, 0.12, 0.11, 0.10, 0.09, 0.13])

# Calculate the expected value
expected_value = np.sum(sales * probabilities)

print(f"Expected number of cars sold per day: {expected_value:.2f}")