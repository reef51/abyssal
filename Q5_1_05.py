# Given data
alpha = 0.10  # Smoothing constant
income_data = [40, 50, 56, 68]  # Income for weeks 1 to 4

# Exponential smoothing forecast calculation
# The forecast for Week 2 is simply the income from Week 1
forecast = income_data[0]

# Loop to calculate the exponential smoothing for Weeks 2 to 4
for week_income in income_data[1:]:
    forecast = alpha * week_income + (1 - alpha) * forecast

# The forecast for Week 5
forecast_week_5 = round(forecast, 2)




print(f"output: {forecast_week_5}")
