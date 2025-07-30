# Given data for Weeks 1 to 10
income_data_week11 = [980, 1040, 1240, 1020, 860, 960, 1080, 1140, 1190, 1040]

# Weights for the 3-week weighted moving average
weights = [0.1, 0.2, 0.7]  # 0.7 for the most current week, 0.1 for the oldest week

# Calculate the 3-week weighted moving average for forecasting Week 11
# Using the income for Weeks 8, 9, and 10
forecast_week_11 = (income_data_week11[-3] * weights[0] + 
                    income_data_week11[-2] * weights[1] + 
                    income_data_week11[-1] * weights[2])

# Round the forecast to the nearest whole number
forecast_week_11_rounded = round(forecast_week_11)



print(f"output: {forecast_week_11_rounded}")
