from scipy.optimize import linprog

# Maximize 
# 167x + 74y
# 120x + 62y <= 800
# 45x + 65y >= -500
# 175x + 45y <= 2000

def solve_linear_program(c, constraints, bounds):
    A_ub = []
    b_ub = []
    constraint_types = []
    
    for constraint in constraints:
        coef, rhs, constraint_type = constraint
        constraint_types.append(constraint_type)  # Store the constraint type
        
        if constraint_type == "<=":
            A_ub.append(coef)
            b_ub.append(rhs)
        elif constraint_type == ">=":
            A_ub.append([-c for c in coef])
            b_ub.append(-rhs)

    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

    if result.success:
        return result.x, -result.fun, result, constraint_types
    else:
        print("No feasible solution found")
        return None, None, None, None

def evaluate_objective(x, y):
    return 2 * x + 1.5 * y

def calculate_slack_or_surplus(x, y, constraints, constraint_types):
    values = []
    terms = []
    for i, (coef, rhs, _) in enumerate(constraints):
        used_value = coef[0] * x + coef[1] * y  # Calculate left-hand side (what's used)
        if constraint_types[i] == "<=":
            surplus = rhs - used_value  # Surplus = right-hand side - used value
            terms.append("surplus")
        else:
            slack = used_value - rhs  # Slack = used value - right-hand side
            terms.append("slack")
        values.append(surplus if constraint_types[i] == "<=" else slack)
    return values, terms

def find_binding_constraints(values, terms):
    binding_constraints = []
    for i, (value, term) in enumerate(zip(values, terms)):
        if value == 0:
            binding_constraints.append(i + 1)  # Use 1-based indexing for constraint numbers
    return binding_constraints

def main():
    # Objective function (maximize 167x + 74y -> minimize -167x - 74y)
    c = [-167, -74]

    # Constraints with their types ("<=" or ">=")
    constraints = [
        ([120, 62], 800, "<="),    # Cutting constraint: 120x + 62y <= 800
        ([45, 65], 1, ">="),    # Assembly constraint: 
        ([175, 45], 2000, "<="),   # Finishing constraint: 175x + 45y <= 2000
        ([50, 30], 1500, "<="),    # New constraint: 50x + 30y <= 1500
    ]

    # Bounds for x and y (x >= 0, y >= 0)
    bounds = [(0, None), (0, None)]

    # Solve the LP using linprog (with both <= and >= constraints)
    lp_solution, lp_value, result, constraint_types = solve_linear_program(c, constraints, bounds)
    
    if lp_solution is not None:
        x, y = lp_solution
        max_profit = lp_value
        print(f"Optimal solution: x = {x:.2f}, y = {y:.2f}")
        print(f"Maximum profit at optimal solution: ${max_profit:.2f}")
        
        # Calculate and print the slack or surplus for each constraint
        values, terms = calculate_slack_or_surplus(x, y, constraints, constraint_types)
        print("\nSlack or Surplus for each constraint:")
        for i, (value, term) in enumerate(zip(values, terms)):
            print(f"Constraint {i + 1} {term}: {value:.2f} minutes")
        
        # Find and print binding constraints (value = 0)
        binding_constraints = find_binding_constraints(values, terms)
        if binding_constraints:
            print("\nBinding Constraints (No slack or surplus):")
            for constraint in binding_constraints:
                print(f"Constraint {constraint} is binding")
        else:
            print("\nNo binding constraints found.")
    else:
        print("No solution found due to infeasibility")

if __name__ == "__main__":
    main()
