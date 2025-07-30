# Given data for each node's expected values
ev_node_6 = 10.2
ev_node_7 = 8
ev_node_8 = 5.7
ev_node_9 = 5.5
ev_node_10 = 9.3
ev_node_11 = 7.5

# Probabilities
p_favorable = 0.7
p_unfavorable = 0.3

# Step 1: Calculate the expected values for Node 3 (Favorable) and Node 4 (Unfavorable)
ev_node_3 = p_favorable * ev_node_6 + p_unfavorable * ev_node_7
ev_node_4 = p_favorable * ev_node_8 + p_unfavorable * ev_node_9

# Step 2: Calculate the expected value for Node 5 (No Review)
ev_node_5 = p_favorable * ev_node_10 + p_unfavorable * ev_node_11

# Step 3: Calculate the overall EV with Sample Information (EV with SI)
ev_with_si = p_favorable * ev_node_3 + p_unfavorable * ev_node_4

ev_with_si


print(f"output: {ev_with_si}")
