# Import necessary libraries
import scipy.stats as stats

# Given values from the problem
multiple_r = 0.7682
r_square = 0.5901
adjusted_r_square = 0.5340
standard_error = 4.3791
observations = 10
significance_f = 0.034
temperature_p_value = 0.0156
significance_level = 0.02

# Check model significance at 0.02 level
def check_model_significance(significance_f, p_value, significance_level):
    model_significant = significance_f < significance_level
    temperature_significant = p_value < significance_level
    if model_significant:
        return f"Yes, because the Significance F of {significance_f} is < {significance_level}"
    else:
        return f"No, because the Significance F of {significance_f} is > {significance_level}"

# Get the significance result for the model
model_significance_message = check_model_significance(significance_f, temperature_p_value, significance_level)

# Print the more relevant result
print(model_significance_message)

# Original code for efficiency calculation
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