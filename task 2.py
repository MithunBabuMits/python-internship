import pandas as pd
import os


file_path = 'StudentsPerformance.csv'

df = pd.read_csv(file_path)
filtered_df = df[df['math score'] > 75]
missing_values = df.isnull().sum()
print(missing_values)


df['math score'].fillna(df['math score'].mean(), inplace=True)
df.dropna(subset=['test preparation course'], inplace=True)

summary_stats = df.describe()
print("Summary statistics for the DataFrame:\n", summary_stats)

mean_age = df['math score'].mean()
median_age = df['math score'].median()
std_age = df['math score'].std()

print(f"Mean math score: {mean_age}")
print(f"Median math score: {median_age}")
print(f"Standard Deviation of math score: {std_age}")