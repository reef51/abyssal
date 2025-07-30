from scipy.stats import poisson

# Parameters
lambda_ = 12
k = 15

# Calculate the probability
probability = poisson.pmf(k, lambda_)
print(probability)
