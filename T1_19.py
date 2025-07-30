from scipy.stats import norm

# Given parameters
mean_age = 67.50
std_dev_age = 16.50
percentile = 0.80

# Calculate the Z-score for the given percentile
z_score = norm.ppf(percentile)

# Convert the Z-score to the actual age
age = mean_age - (z_score * std_dev_age)

print(f"The age such that 80% of high schools are older than it is: {age:.2f} years")
