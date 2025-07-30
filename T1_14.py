from scipy.stats import expon

# Average time between ticket orders (mean)
mean_time = 75

# Rate parameter (lambda) for the exponential distribution
lambda_rate = 1 / mean_time

# Time of interest
time_of_interest = 30

# Calculate the probability that the next ticket arrives in less than 30 seconds
probability_less_than_30 = expon.cdf(time_of_interest, scale=mean_time)

print(f"Probability that the next ticket arrives in less than {time_of_interest} seconds: {probability_less_than_30:.4f}")
