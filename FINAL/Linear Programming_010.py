from scipy.optimize import linprog

"""
3x + 3y
1x + 2y <= 16
1x + 1y <= 10
5x + 3y <= 45
"""


# Objective function (maximize 10x + 5y -> minimize -10x - 5y)
c = [-10, -5]

# Constraints with their coefficients and right-hand side values
A = [2, 4]
B = [3, 1]
C = [1, 4]
b_ub = [100, 90, 80]

# Constraints for linprog
A_ub = [A, B, C]

# Bounds for x and y (x >= 0, y >= 0)
bounds = [(0, None), (0, None)]

# Solve the LP using linprog
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

if result.success:
    x, y = result.x
    print(f"Optimal solution: x = {x:.2f}, y = {y:.2f}")
    print(f"Maximum value of the objective function: {10 * x + 5 * y:.2f}")

    # Check which constraints are binding
    slack_values = result.slack
    binding_constraints = [i + 1 for i, slack in enumerate(slack_values) if slack == 0]
    print("\nBinding Constraints:")
    for constraint in binding_constraints:
        print(f"Constraint {constraint}")
else:
    print("No feasible solution found")
