import pandas as pd
import numpy as np

# Create a DataFrame with the sales data
data_sales = {
    "Week": [1, 2, 3, 4, 5, 6],
    "Sales": [58, 70, 50, 62, 66, 70]
}

df_sales = pd.DataFrame(data_sales)

# Calculate the 2-week simple moving average starting from Week 3
df_sales['2-week SMA'] = df_sales['Sales'].rolling(window=2).mean()

# Calculate the forecast errors (only for weeks where we have forecasts)
df_sales['Error'] = df_sales['Sales'] - df_sales['2-week SMA']

# Calculate the squared errors
df_sales['Squared Error'] = df_sales['Error']**2

# Calculate Mean Squared Error (MSE)
mse = np.nanmean(df_sales['Squared Error'])

# Display the results
print(df_sales)
print(f"Mean Square Error (MSE): {mse:.0f}")
