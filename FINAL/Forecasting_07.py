# Given income data for 4 weeks
income = [350, 380, 450]

# Smoothing constant
alpha = 0.10

# Initialize the first forecast as the first income value
forecast = [income[0]]

# Calculate the exponential smoothing forecasts
for i in range(1, len(income)):
    new_forecast = alpha * income[i-1] + (1 - alpha) * forecast[-1]
    forecast.append(new_forecast)

# Forecast for Week 3 and Week 4
forecast_week_3 = forecast[2]
forecast_week_4 = alpha * income[2] + (1 - alpha) * forecast[2]

# Calculate the difference between Week 4 and Week 3 forecasts
difference = forecast_week_4 - forecast_week_3

# Print the difference rounded to two decimal places
print(f"Difference between Week 4 and Week 3 forecasts: {difference:.2f}")
