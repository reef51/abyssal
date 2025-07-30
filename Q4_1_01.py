# Regression equation coefficients
intercept = 50    # Intercept from the regression output
slope = 7.21      # Coefficient for Interest Rate %

# Function to calculate deposits based on interest rate
def calculate_deposits(interest_rate):
    return intercept + slope * interest_rate

# Example: Calculate deposits for interest rates from 0% to 10%
interest_rates = [i for i in range(0, 11)]  # Interest rates from 0% to 10%
deposits = [calculate_deposits(rate) for rate in interest_rates]

# Display the results
for rate, deposit in zip(interest_rates, deposits):
    print(f"Interest Rate: {rate}% -> Deposits: {deposit}")

# Calculate the increase in deposits for each 1% increase in interest rate
increase_per_percent = slope  # From the regression coefficient
print(f"\nFor each 1% increase in interest rate, deposits increase by: {increase_per_percent}")
