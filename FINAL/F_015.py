# Calculate Mean Squared Error (MSE) for Naive Method and 2-week Simple Moving Average
import numpy as np

def calculate_naive_forecast(data):
    naive_forecast = [None] + data[:-1]  # Naive forecast shifts the data by 1
    return naive_forecast

def calculate_2_week_sma(data):
    sma_forecast = [None, None]  # First two weeks have no forecast
    for i in range(2, len(data)):
        sma_forecast.append((data[i-1] + data[i-2]) / 2)
    return sma_forecast

def calculate_mse(actual, forecast):
    errors = [(a - f) ** 2 for a, f in zip(actual, forecast) if f is not None]
    mse = np.mean(errors)
    return mse

# Given data
sales_data = [21, 28, 26, 33, 37, 41]

# Calculate forecasts
naive_forecast = calculate_naive_forecast(sales_data)
sma_forecast = calculate_2_week_sma(sales_data)

# Calculate Mean Squared Errors
mse_naive = calculate_mse(sales_data, naive_forecast)
mse_sma = calculate_mse(sales_data, sma_forecast)

# Determine which method is more accurate and the difference in MSE
if mse_naive < mse_sma:
    better_method = "Naive"
    mse_difference = mse_sma - mse_naive
else:
    better_method = "2-week Simple Moving Average"
    mse_difference = mse_naive - mse_sma

# Output the results
print(f"Better Forecasting Method: {better_method}")
print(f"Difference in MSE: {mse_difference:.2f}")