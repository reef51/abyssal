# Given data for Weeks 1 to 3
alpha = 0.10  # Smoothing constant
income_data_weeks3_4 = [350, 380, 450]  # Income for weeks 1 to 3

# Exponential smoothing forecast calculation
# The forecast for Week 2 is simply the income from Week 1
forecast_week2 = income_data_weeks3_4[0]

# Loop to calculate the exponential smoothing for Weeks 2 and 3
for week_income in income_data_weeks3_4[1:]:
    forecast_week2 = alpha * week_income + (1 - alpha) * forecast_week2

# The forecast for Week 3 is the final forecast after the above loop
forecast_week_3 = forecast_week2

# Forecast for Week 4 (using the income from Week 3 and the forecast for Week 3)
forecast_week_4 = alpha * income_data_weeks3_4[2] + (1 - alpha) * forecast_week_3

# Calculate the difference between the forecast for Week 3 and Week 4
forecast_difference = round(abs(forecast_week_4 - forecast_week_3), 2)






print(f"output: {forecast_difference}")
