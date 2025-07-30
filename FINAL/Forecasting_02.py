import numpy as np

# Given sales data for 6 weeks
sales = [58, 70, 50, 62, 66, 70]

# Calculate the forecasts using a two-week simple moving average
forecasts = []
for i in range(2, len(sales)):
    forecast = (sales[i-1] + sales[i-2]) / 2
    forecasts.append(forecast)

# Calculate the errors and Mean Square Error (MSE)
errors = [sales[i] - forecasts[i-2] for i in range(2, len(sales))]
squared_errors = [error**2 for error in errors]
mse = np.mean(squared_errors)

# Print the Mean Square Error (MSE) rounded to the nearest whole number
mse_rounded = round(mse)
print(f"Mean Square Error (MSE): {mse_rounded}")
