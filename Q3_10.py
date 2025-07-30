from scipy.stats import binom

# Parameters
n = 8
p = 0.40
k = 5

# Probability
probability = binom.pmf(k, n, p)
print(probability)
