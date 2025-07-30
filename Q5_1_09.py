# Given data for Weeks 1 to 5
income_data_week6 = [690, 840, 700, 720, 860]

# Weights for the 3-week weighted moving average
weights_week6 = [0.5, 0.4, 0.1]  # 0.5 for the most current week, 0.1 for the oldest week

# Calculate the 3-week weighted moving average for forecasting Week 6
# Using the income for Weeks 3, 4, and 5
forecast_week_6 = (income_data_week6[-1] * weights_week6[0] + 
                   income_data_week6[-2] * weights_week6[1] + 
                   income_data_week6[-3] * weights_week6[2])

# Round the forecast to the nearest whole number
forecast_week_6_rounded = round(forecast_week_6)





print(f"output: {forecast_week_6_rounded}")
