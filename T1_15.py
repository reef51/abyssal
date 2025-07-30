# Given probabilities
P_rainy = 0.80
P_delay = 0.90
P_clear_given_no_delay = 0.60

# Probability of no delay
P_no_delay = 1 - P_delay

# Probability of clear weather given no delays
P_clear_given_no_delay = P_clear_given_no_delay * P_no_delay

# Probability of clear weather
P_clear = 1 - P_rainy

# Probability of clear weather and delay
P_clear_and_delay = P_clear - P_clear_given_no_delay

# Probability of rainy weather and delay
P_rainy_and_delay = P_delay - P_clear_and_delay

print(f"Probability of rainy weather and delays: {P_rainy_and_delay:.4f}")
