import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Data Preparation
# Load the dataset
url = 'https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)

# Data Cleaning
# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Step 3: Exploratory Visual Analysis
# Overview of the Dataset
# Explore basic statistics
print(df.describe())

# Investigate trends in crime rates over the years
plt.figure(figsize=(10, 6))
df['Year'] = df['Date'].dt.year
crime_by_year = df['Year'].value_counts().sort_index()
sns.lineplot(x=crime_by_year.index, y=crime_by_year.values)
plt.title('Trends in Crime Rates Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.show()

# Spatial Patterns of Criminal Activity
plt.figure(figsize=(10, 8))
sns.scatterplot(x='Longitude', y='Latitude', data=df, alpha=0.01)
plt.title('Spatial Patterns of Criminal Activity')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

# Variation of Crime Types by Time
df['Hour'] = df['Date'].dt.hour
plt.figure(figsize=(10, 6))
sns.countplot(x='Hour', data=df, hue='Primary Type')
plt.title('Variation of Crime Types by Time')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Crimes')
plt.legend(title='Crime Type', loc='upper right', bbox_to_anchor=(1.25, 1))
plt.show()

# Step 4: Conclusion
# Summary of Findings
# General Conclusion
# In this project, we have explored the Chicago Crimes dataset and identified trends, spatial patterns, and variations in crime types over time. Further analysis and actions can be taken based on these insights.

