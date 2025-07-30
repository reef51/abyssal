import scipy.stats as stats

# Given average rate (lambda) for 60 minutes
lambda_60 = 15

# Calculate P(X >= 14)
p_x_geq_14 = 1 - stats.poisson.cdf(13, lambda_60)

print(f"Probability of 14 or more customers: {p_x_geq_14:.4f}")
