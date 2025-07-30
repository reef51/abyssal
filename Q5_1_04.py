import pandas as pd

# Updated DataFrame with the sales data for 10 weeks
data_forecast_updated = {
    "Period": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Sales": [250, 230, 210, 190, 210, 220, 250, 170, 190]
}

df_forecast_updated = pd.DataFrame(data_forecast_updated)

# Calculate the 4-period simple moving average for forecasting Week 10
df_forecast_updated['4-period SMA'] = df_forecast_updated['Sales'].rolling(window=4).mean()

# Forecast for Week 10 is the 4-period moving average of periods 6 to 9
forecast_week_10_updated = df_forecast_updated['Sales'].iloc[-4:].mean()

# Round the forecast to the nearest whole number
forecast_week_10_updated_rounded = round(forecast_week_10_updated)

# Display the forecast
forecast_week_10_updated_rounded

# Display the forecast for Week 10
print(f"Forecast for Week 10: {forecast_week_10_updated_rounded}")
