# Calculate Expected Value with Perfect Information (EVwPI)

# Given probabilities
prob_s1 = 0.30
prob_s2 = 0.70

# Payoffs for each decision under different states
payoff_a_s1, payoff_a_s2 = 2, 6
payoff_b_s1, payoff_b_s2 = 11, 6
payoff_c_s1, payoff_c_s2 = 1, 14
payoff_d_s1, payoff_d_s2 = 10, 8

# Determine the best payoff for each state of nature
best_s1 = max(payoff_a_s1, payoff_b_s1, payoff_c_s1, payoff_d_s1)
best_s2 = max(payoff_a_s2, payoff_b_s2, payoff_c_s2, payoff_d_s2)

# Calculate EVwPI
evwpi = (prob_s1 * best_s1) + (prob_s2 * best_s2)

# Output the result
print(f"Expected Value with Perfect Information (EVwPI): {evwpi:.2f}")

# Excel output format
print(f"=({prob_s1} * {best_s1}) + ({prob_s2} * {best_s2})")