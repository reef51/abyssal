from scipy.optimize import linprog

"""
MAX
3x + 7y

3y ≤ 9
4x + 2y ≤ 20
3x + 6y ≤ 24
x, y ≥ 0
"""

def solve_linear_program(c, constraints, bounds, maximize=True):
    A_ub = []
    b_ub = []
    constraint_types = []
    
    for constraint in constraints:
        coef, rhs, constraint_type = constraint
        constraint_types.append(constraint_type)  # Store the constraint type
        
        if constraint_type == "<=" or constraint_type == "<":
            A_ub.append(coef)
            b_ub.append(rhs)
        elif constraint_type == ">=" or constraint_type == ">":
            A_ub.append([-c for c in coef])
            b_ub.append(-rhs)

    # For maximization, minimize the negative of the objective function
    if maximize:
        c = [-coef for coef in c]
    
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

    if result.success:
        return result.x, -result.fun if maximize else result.fun, result, constraint_types
    else:
        print("No feasible solution found")
        return None, None, None, None

def calculate_slack_or_surplus(x1, x2, constraints, constraint_types):
    values = []
    terms = []
    for i, (coef, rhs, _) in enumerate(constraints):
        used_value = coef[0] * x1 + coef[1] * x2  # Calculate left-hand side (what's used)
        if constraint_types[i] == "<=" or constraint_types[i] == "<":
            surplus = rhs - used_value  # Surplus = right-hand side - used value
            terms.append("slack")
        else:
            slack = used_value - rhs  # Slack = used value - right-hand side
            terms.append("surplus")
        values.append(surplus if constraint_types[i] == "<=" or constraint_types[i] == "<" else slack)
    return values, terms

def find_binding_constraints(values, terms):
    binding_constraints = []
    for i, (value, term) in enumerate(zip(values, terms)):
        if value == 0:
            binding_constraints.append(i + 1)  # Use 1-based indexing for constraint numbers
    return binding_constraints

def main():
    # Objective function (3x + 7y)
    c = [3, 7]

    # Constraints with their types ("<=" or ">=")
    constraints = [
        ([0, 3], 9, "<="),     # 3y ≤ 9
        ([4, 2], 20, "<="),    # 4x + 2y ≤ 20
        ([3, 6], 24, "<="),    # 3x + 6y ≤ 24
    ]

    # Bounds for x and y (x ≥ 0, y ≥ 0)
    bounds = [(0, None), (0, None)]

    # Solve the LP for maximization
    print("Maximization Problem:")
    lp_solution_max, lp_value_max, result_max, constraint_types_max = solve_linear_program(c, constraints, bounds, maximize=True)
    
    if lp_solution_max is not None:
        x1_max, x2_max = lp_solution_max
        print(f"Optimal solution for maximization: x1 = {x1_max:.2f}, x2 = {x2_max:.2f}")
        print(f"Maximum profit: ${lp_value_max:.2f}")
        
        values_max, terms_max = calculate_slack_or_surplus(x1_max, x2_max, constraints, constraint_types_max)
        print("\nSlack or Surplus for each constraint in maximization:")
        for i, (value, term) in enumerate(zip(values_max, terms_max)):
            print(f"Constraint {i + 1} {term}: {value:.2f}")
        
        binding_constraints_max = find_binding_constraints(values_max, terms_max)
        if binding_constraints_max:
            print("\nBinding Constraints (No slack or surplus) in maximization:")
            for constraint in binding_constraints_max:
                print(f"Constraint {constraint} is binding")
        else:
            print("\nNo binding constraints found in maximization.")
    else:
        print("No solution found for maximization due to infeasibility.")

if __name__ == "__main__":
    main()