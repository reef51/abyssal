# Sensitivity Analysis to Determine Best Decision

def calculate_expected_values():
    # Probabilities
    prob_s1 = 0.75
    prob_s2 = 0.25

    # Payoffs for each decision
    payoff_A_s1, payoff_A_s2 = 6, 2
    payoff_B_s1, payoff_B_s2 = 1, 14
    payoff_C_s1, payoff_C_s2 = 3, 10

    # Calculate Expected Values
    ev_A = (prob_s1 * payoff_A_s1) + (prob_s2 * payoff_A_s2)
    ev_B = (prob_s1 * payoff_B_s1) + (prob_s2 * payoff_B_s2)
    ev_C = (prob_s1 * payoff_C_s1) + (prob_s2 * payoff_C_s2)

    # Determine the best decision based on expected values
    decisions = {'A': ev_A, 'B': ev_B, 'C': ev_C}
    best_decision = max(decisions, key=decisions.get)

    return decisions, best_decision

# Output the results
decisions, best_decision = calculate_expected_values()
for decision, value in decisions.items():
    print(f"Expected Value of Decision {decision}: {value:.2f}")
print(f"Best Decision: {best_decision}")