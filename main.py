import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# **********************************************************************************************************************
# Q1) How does temperature vary throughout the year? Are there distinct seasonal patterns?
# Q2) Are there any noticeable trends or patterns in wind speed over the course of the year?
# Q3) Are there any noticeable trends or patterns in the amount of precipitation over the course of the year?
# **********************************************************************************************************************

# 1) Load the dataset
df = pd.read_csv('weather.csv')

# 2) Data Cleaning
# fill rows with missing values with "0"
df.fillna("0", inplace=True)
pd.set_option('display.max_columns', None)

# 3) Convert 'date' column to datetime instead of string
df['date'] = df['date'].apply(lambda x: datetime.strptime(str(x), '%Y%m%d').date())

# 4) Exploratory Visual Analysis
# Overview of the Dataset
# Explore basic statistics

# Question 1: How does temperature vary throughout the year? Are there distinct seasonal patterns?
# Extract month from the 'date' column
df['month'] = pd.to_datetime(df['date']).dt.month

df['TAVG'] = pd.to_numeric(df['TAVG'], errors='coerce')

avg_temp_by_month = df.groupby("month")["TAVG"].mean()

# Plotting the average temperature variation throughout the year
plt.figure(figsize=(10, 6))
avg_temp_by_month.plot(kind="bar", color='skyblue')
plt.title("Average Temperature Variation Throughout the Year", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Average Temperature (°F)", fontsize=14)
plt.xticks(range(0, 12), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
           rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Q1) How does temperature vary throughout the year? Are there distinct seasonal patterns? Explanation: The bar plot
# shows the average temperature variation throughout the year, with each bar representing a month. From the plot,
# we can observe that temperatures tend to be lower in the winter months (December to February) and higher in the
# summer months (June to August), indicating a seasonal pattern. There is a gradual increase in temperature from
# spring to summer and a decrease from summer to winter.


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Question 2 : Are there any noticeable trends or patterns in wind speed over the course of the year?

# Extract month from the 'date' column
df['month'] = pd.to_datetime(df['date']).dt.month

# Convert 'WSF5' column to numeric, coercing errors to NaN
df['WSF5'] = pd.to_numeric(df['WSF5'], errors='coerce')

# Group data by month and calculate average wind speed
avg_wind_speed_by_month = df.groupby('month')['WSF5'].mean()

# Plotting the variation in wind speed levels over the course of the year
plt.figure(figsize=(10, 6))
plt.plot(avg_wind_speed_by_month.index, avg_wind_speed_by_month.values, marker='o', linestyle='-')
plt.title("Average Wind Speed Variation Throughout the Year")
plt.xlabel("Month")
plt.ylabel("Average Wind Speed (mph)")
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Q2) Are there any noticeable trends or patterns in wind speed over the course of the year?
# Explanation: The line plot shows the variation in average wind speed over the course of the year. By analyzing this
# plot, we can identify any trends or patterns in wind speed levels across different months. For example, we may observe
# higher wind speeds during certain seasons or months, indicating seasonal patterns or trends in wind behavior.


# Question 3 : Are there any noticeable trends or patterns in the amount of precipitation over the course of the year?

# Extract month from the 'date' column
df['month'] = pd.to_datetime(df['date']).dt.month

# Convert 'PRCP' column to numeric, coercing errors to NaN
df['PRCP'] = pd.to_numeric(df['PRCP'], errors='coerce')

# Group data by month and calculate average precipitation
avg_precip_by_month = df.groupby('month')['PRCP'].mean()

# Plotting the variation in precipitation levels over the course of the year
plt.figure(figsize=(10, 6))
plt.plot(avg_precip_by_month.index, avg_precip_by_month.values, marker='o', linestyle='-')
plt.title("Average Precipitation Variation Throughout the Year")
plt.xlabel("Month")
plt.ylabel("Average Precipitation (inches)")
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Q3) Are there any noticeable trends or patterns in the amount of precipitation over the course of the year?
#
# Explanation: To answer this question, you can refer to the visualizations of precipitation over time. You might
# observe certain months or seasons with higher or lower precipitation levels, indicating trends or patterns. For
# example, if there's a spike in precipitation during the summer months, it might suggest a rainy season. Similarly,
# if precipitation is consistently low during certain months, it might indicate a dry season.


