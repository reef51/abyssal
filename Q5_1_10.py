# Given data for Weeks 1 to 7
income_data_week8 = [150, 120, 240, 220, 160, 190, 210]

# Weights for the 3-week weighted moving average
weights_week8 = [0.1, 0.3, 0.6]  # 0.6 for the most current week, 0.1 for the oldest week

# Calculate the 3-week weighted moving average for forecasting Week 8
# Using the income for Weeks 5, 6, and 7
forecast_week_8 = (income_data_week8[-1] * weights_week8[2] + 
                   income_data_week8[-2] * weights_week8[1] + 
                   income_data_week8[-3] * weights_week8[0])

# Round the forecast to the nearest whole number
forecast_week_8_rounded = round(forecast_week_8)


print(f"output: {forecast_week_8_rounded}")
