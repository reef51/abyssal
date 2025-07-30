import pandas as pd

# Create a DataFrame with the sales data up to Week 9
data_forecast = {
    "Period": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Sales": [250, 230, 210, 190, 175, 202, 215, 168, 174]
}

df_forecast = pd.DataFrame(data_forecast)

# Calculate the 4-period simple moving average for forecasting Week 10
df_forecast['4-period SMA'] = df_forecast['Sales'].rolling(window=4).mean()

# Forecast for Week 10 is the 4-period moving average of periods 6 to 9
forecast_week_10 = df_forecast['Sales'].iloc[-4:].mean()

# Round the forecast to the nearest whole number
forecast_week_10_rounded = round(forecast_week_10)

# Display the forecast for Week 10
print(f"Forecast for Week 10: {forecast_week_10_rounded}")
