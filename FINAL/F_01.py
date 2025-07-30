# Given probabilities
P_X = 0.60
P_Y = 0.42
P_Y_given_X = 0.20

# Calculating P(X and Y)
P_X_and_Y = P_Y_given_X * P_X

# Calculating P(X | Y)
P_X_given_Y = P_X_and_Y / P_Y

# Calculating P(NOT X | Y)
P_not_X_given_Y = 1 - P_X_given_Y

# Output the result
print(f"P(NOT X | Y): {P_not_X_given_Y:.4f}")