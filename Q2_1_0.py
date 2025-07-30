# 1. Define the expected payoff function for Venture B
def expected_payoff_B(p):
    return 4 * p - 2

# 2. Define the expected payoff function for Venture C
def expected_payoff_C(p):
    return -4 * p + 1

# 3. Function to find the probability at which the two ventures have the same expected payoff
def find_indifference_point():
    # Set the equation for expected payoffs to be equal: 4p - 2 = -4p + 1
    # Solving the equation manually gives p = 3/8 = 0.375
    indifference_point = 3 / 8
    return indifference_point

# 4. Calculate the indifference probability
probability = find_indifference_point()

# 5. Print the result
print(f"The probability of prosperity at which the company is indifferent between Venture B and Venture C is: {probability:.3f}")
