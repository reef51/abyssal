import scipy.stats as stats

# Given values
mean = 93
std_dev = 15
percentile = 0.80

# Calculate the value at the 80th percentile (since we need 80% or more)
x_value = stats.norm.ppf(percentile, mean, std_dev)

# Output the result
print(f"Number of grapes for 80% probability: {x_value:.2f}")