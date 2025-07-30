from scipy.stats import binom

# Parameters
n = 30  # number of students
p = 0.15  # probability of becoming fluent

# Calculate probability of fewer than 3 students becoming fluent
probability_fewer_than_3 = binom.cdf(2, n, p)

print("Probability that fewer than 3 students become fluent:", probability_fewer_than_3)
