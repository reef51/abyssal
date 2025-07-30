from scipy.optimize import linprog

def solve_linear_program(c, constraints, bounds):
    A_ub = []
    b_ub = []
    
    for constraint in constraints:
        coef, rhs, constraint_type = constraint
        
        if constraint_type == "<=":
            A_ub.append(coef)
            b_ub.append(rhs)
        elif constraint_type == ">=":
            A_ub.append([-c for c in coef])
            b_ub.append(-rhs)

    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

    if result.success:
        return result.x, -result.fun, result
    else:
        return None, None, None

def evaluate_objective(x, y):
    return 2 * x + 1.5 * y

def find_feasible_vertices():
    # Manually derived intersection points (feasible region vertices)
    vertices = [
        (0, 0),  # Origin
        (2, 0),  # x = 2, y = 0 (x <= 2, y = 0)
        (0, 4),  # Intersection of 4x + 6y = 24 with x = 0
        (2, 1),  # Intersection of 5x + 5y = 15 and x = 2
    ]
    return vertices

def solve_lp_with_manual_vertices():
    vertices = find_feasible_vertices()
    optimal_value = float('-inf')
    optimal_solution = None

    for vertex in vertices:
        x, y = vertex
        Z = evaluate_objective(x, y)
        print(f"At point ({x}, {y}), Z = {Z:.2f}")

        if Z > optimal_value:
            optimal_value = Z
            optimal_solution = vertex

    return optimal_solution, optimal_value

def check_binding_constraints(result, constraints):
    tolerance = 1e-6
    print("\nBinding Constraints Check:")
    for i, (coef, rhs, _) in enumerate(constraints):
        if abs(sum([coef[j] * result.x[j] for j in range(len(coef))]) - rhs) < tolerance:
            print(f"Constraint {i + 1} is binding.")
        else:
            print(f"Constraint {i + 1} is not binding.")

def main():
    # Objective function (maximize 2x + 1.5y -> minimize -2x - 1.5y)
    c = [-2, -1.5]

    # Constraints with their types ("<=" or ">=")
    constraints = [
        ([4, 6], 24, "<="),   # 4x + 6y <= 24
        ([5, 5], 15, "<="),   # 5x + 5y <= 15
        ([1, 0], 2, "<="),    # x <= 2
    ]

    # Bounds for x and y (x >= 0, y >= 0)
    bounds = [(0, None), (0, None)]

    # Solve the LP using linprog (with both <= and >= constraints)
    lp_solution, lp_value, result = solve_linear_program(c, constraints, bounds)
    if lp_solution is not None:
        print(f"Optimal solution from linprog: x = {lp_solution[0]:.2f}, y = {lp_solution[1]:.2f}, Profit = ${lp_value:.2f}")
        check_binding_constraints(result, constraints)
    else:
        print("No solution found using linprog.")

    # Solve the LP using manual corner points evaluation
    manual_solution, manual_value = solve_lp_with_manual_vertices()
    print(f"Optimal solution using manual corner points: x = {manual_solution[0]:.2f}, y = {manual_solution[1]:.2f}, Profit = ${manual_value:.2f}")

if __name__ == "__main__":
    main()
