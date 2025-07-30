# Define the values given
EV_with_SI = 25
EV_without_SI = 20
EV_with_PI = 50
EV_without_PI = 40

# Calculate the efficiency of Sample Information (SI)
def calculate_efficiency(EV_with_SI, EV_without_SI, EV_with_PI, EV_without_PI):
    efficiency_SI = (EV_with_SI - EV_without_SI) / (EV_with_PI - EV_without_PI)
    return efficiency_SI

# Calculate the efficiency
efficiency = calculate_efficiency(EV_with_SI, EV_without_SI, EV_with_PI, EV_without_PI)

# Print the result
print(f"Efficiency of Sample Information: {efficiency:.3f}")
