# Import necessary libraries

# Umbrella Profit Maximization Problem
"""
Maximize: 4w + 6g + 5m + 3.5f
Subject to:
1) Storage: w + g + m + f <= 120
2) Marketing Restriction: w + g + m + f <= 12
3) Space constraint: w + g + m + f <= 72 (new constraint added for testing)
"""

# Given shadow prices and allowable changes from the problem statement
shadow_prices = [2, 1.5]  # Shadow prices for Space and Demand constraints
changes = [20, 12]  # Changes: +20 units to Space, +12 units to Demand
allowable_increases = [48, 24]  # Allowable increases for Space and Demand
allowable_decreases = [24, 48]  # Allowable decreases for Space and Demand

def calculate_new_objective_value_with_100_percent_rule(original_value, shadow_prices, changes, allowable_increases, allowable_decreases):
    # Apply the 100% rule to ensure simultaneous changes are valid
    total_proportion = 0
    for change, allowable_increase, allowable_decrease in zip(changes, allowable_increases, allowable_decreases):
        if change > 0 and allowable_increase != float('inf'):
            total_proportion += change / allowable_increase
        elif change < 0 and allowable_decrease != float('inf'):
            total_proportion += abs(change) / allowable_decrease
    
    # If the total proportion exceeds 1, the changes are not allowed simultaneously
    if total_proportion > 1:
        print("Simultaneous changes exceed allowable limits based on the 100% rule. No changes applied.")
        return original_value
    
    # Calculate the impact on the objective function value based on shadow prices and changes
    total_change = 0
    for shadow_price, change in zip(shadow_prices, changes):
        total_change += shadow_price * change
    
    # Ensure the new value is rounded to match expected precision
    new_value = round(original_value + total_change, 2)
    return new_value

def main():
    # Original maximum profit value
    original_value = 318  # Updated original profit value to match the correct calculation
    print(f"Original objective function value: ${original_value:.2f}")
    
    # Calculate the new objective function value using the 100% rule
    new_objective_value = calculate_new_objective_value_with_100_percent_rule(original_value, shadow_prices, changes, allowable_increases, allowable_decreases)
    print(f"New objective function value after changes: ${new_objective_value:.2f}")

if __name__ == "__main__":
    main()