import numpy as np

# Sales (Number of Cars Sold) and their respective probabilities
sales = np.array([0, 1, 2, 3, 4, 5])
probabilities = np.array([0.45, 0.12, 0.11, 0.10, 0.09, 0.13])

# Calculate the expected value
expected_value = np.sum(sales * probabilities)

print(f"Expected number of cars sold per day: {expected_value:.2f}")

# Step 1: Calculate Expected Values Without Forecast
P_S1 = 0.80
P_S2 = 1 - P_S1

def calculate_expected_value(payoff_s1, payoff_s2, P_S1, P_S2):
    return (payoff_s1 * P_S1) + (payoff_s2 * P_S2)

# Payoffs for decisions P, Q, R
ev_p = calculate_expected_value(11, 8, P_S1, P_S2)
ev_q = calculate_expected_value(5, 13, P_S1, P_S2)
ev_r = calculate_expected_value(15, 4, P_S1, P_S2)

print(f"Expected Value for Decision P: {ev_p:.2f}")
print(f"Expected Value for Decision Q: {ev_q:.2f}")
print(f"Expected Value for Decision R: {ev_r:.2f}")

# Best expected value without forecast
best_ev_without_forecast = max(ev_p, ev_q, ev_r)
print(f"Best Expected Value Without Forecast: {best_ev_without_forecast:.2f}")

# Step 2: Calculate Expected Value With Perfect Information
max_s1 = max(11, 5, 15)  # Maximum value for S1
max_s2 = max(8, 13, 4)    # Maximum value for S2

ev_with_forecast = (max_s1 * P_S1) + (max_s2 * P_S2)
print(f"Expected Value With Perfect Information: {ev_with_forecast:.2f}")

# Step 3: Calculate the Value of Perfect Information (VPI)
vpi = ev_with_forecast - best_ev_without_forecast
print(f"Value of Perfect Information (VPI): {vpi:.2f}")