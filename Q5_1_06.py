# Given data for Weeks 1 to 6
alpha = 0.30  # Smoothing constant
income_data_week7 = [80, 100, 126, 138, 130, 120]  # Income for weeks 1 to 6

# Exponential smoothing forecast calculation
# The forecast for Week 2 is simply the income from Week 1
forecast_week7 = income_data_week7[0]

# Loop to calculate the exponential smoothing for Weeks 2 to 6
for week_income in income_data_week7[1:]:
    forecast_week7 = alpha * week_income + (1 - alpha) * forecast_week7

# The forecast for Week 7
forecast_week_7 = round(forecast_week7, 2)



print(f"output: {forecast_week_7}")
