from scipy.optimize import linprog

"""
3x + 3y
1x + 2y <= 16
1x + 1y <= 10
5x + 3y <= 45
"""

def solve_linear_program(c, constraints, bounds, maximize=True):
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

    # For maximization, minimize the negative of the objective function
    if maximize:
        c = [-coef for coef in c]
    
    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

    if result.success:
        return result.x, -result.fun if maximize else result.fun, result, constraint_types
    else:
        print("No feasible solution found")
        return None, None, None, None

def calculate_slack_or_surplus(X1, X2, constraints, constraint_types):
    values = []
    terms = []
    for i, (coef, rhs, _) in enumerate(constraints):
        used_value = coef[0] * X1 + coef[1] * X2  # Calculate left-hand side (what's used)
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
    # Objective function (50X1 + 20X2)
    c = [50, 20]

    # Constraints with their types ("<=" or ">=")
    constraints = [
        ([1, 2], 45, "<="),   # X1 + 2X2 <= 45
        ([3, 3], 87, "<="),   # 3X1 + 3X2 <= 87
        ([2, 1], 50, "<="),   # 2X1 + X2 <= 50
    ]

    # Bounds for X1 and X2 (X1 >= 0, X2 >= 0)
    bounds = [(0, None), (0, None)]

    # Solve the LP for maximization
    print("Maximization Problem:")
    lp_solution_max, lp_value_max, result_max, constraint_types_max = solve_linear_program(c, constraints, bounds, maximize=True)
    
    if lp_solution_max is not None:
        X1_max, X2_max = lp_solution_max
        print(f"Optimal solution for maximization: X1 = {X1_max:.2f}, X2 = {X2_max:.2f}")
        print(f"Maximum revenue: ${lp_value_max:.2f}")
        
        values_max, terms_max = calculate_slack_or_surplus(X1_max, X2_max, constraints, constraint_types_max)
        print("\nSlack or Surplus for each constraint in maximization:")
        for i, (value, term) in enumerate(zip(values_max, terms_max)):
            print(f"Constraint {i + 1} {term}: {value:.2f} minutes")
        
        binding_constraints_max = find_binding_constraints(values_max, terms_max)
        if binding_constraints_max:
            print("\nBinding Constraints (No slack or surplus) in maximization:")
            for constraint in binding_constraints_max:
                print(f"Constraint {constraint} is binding")
        else:
            print("\nNo binding constraints found in maximization.")
    else:
        print("No solution found for maximization due to infeasibility.")

    # Solve the LP for minimization
    print("\nMinimization Problem:")
    lp_solution_min, lp_value_min, result_min, constraint_types_min = solve_linear_program(c, constraints, bounds, maximize=False)
    
    if lp_solution_min is not None:
        X1_min, X2_min = lp_solution_min
        print(f"Optimal solution for minimization: X1 = {X1_min:.2f}, X2 = {X2_min:.2f}")
        print(f"Minimum revenue: ${lp_value_min:.2f}")
        
        values_min, terms_min = calculate_slack_or_surplus(X1_min, X2_min, constraints, constraint_types_min)
        print("\nSlack or Surplus for each constraint in minimization:")
        for i, (value, term) in enumerate(zip(values_min, terms_min)):
            print(f"Constraint {i + 1} {term}: {value:.2f} minutes")
        
        binding_constraints_min = find_binding_constraints(values_min, terms_min)
        if binding_constraints_min:
            print("\nBinding Constraints (No slack or surplus) in minimization:")
            for constraint in binding_constraints_min:
                print(f"Constraint {constraint} is binding")
        else:
            print("\nNo binding constraints found in minimization.")
    else:
        print("No solution found for minimization due to infeasibility.")

if __name__ == "__main__":
    main()
