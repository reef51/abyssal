# Calculate Expected Value with Sample Information (EVSI)

def calculate_evsi():
    # Probabilities and Payoffs
    favorable_prob = 0.40
    unfavorable_prob = 0.60

    # Payoffs for Node 3 (Favorable)
    large_favorable = 0.9 * 12 + 0.1 * 2
    small_favorable = 0.9 * 9 + 0.1 * 5
    ev_node_3 = max(large_favorable, small_favorable)

    # Payoffs for Node 4 (Unfavorable)
    large_unfavorable = 0.4 * 12 + 0.6 * 2
    small_unfavorable = 0.4 * 9 + 0.6 * 5
    ev_node_4 = max(large_unfavorable, small_unfavorable)

    # Expected Value for Review Branch
    ev_review = favorable_prob * ev_node_3 + unfavorable_prob * ev_node_4

    # Payoffs for Node 5 (No Review)
    large_no_review = 0.8 * 12 + 0.2 * 2
    small_no_review = 0.8 * 9 + 0.2 * 5
    ev_node_5 = max(large_no_review, small_no_review)

    # Expected Value with Sample Information
    evsi = max(ev_review, ev_node_5)

    return evsi

# Output the result
evsi = calculate_evsi()
print(f"Expected Value with Sample Information: {evsi:.2f}")