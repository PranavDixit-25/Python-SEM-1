import pandas as pd

data = pd.read_csv('abd.csv')

print("Number of rows:", data.shape[0])
print("Number of columns:", data.shape[1])

print("\nFirst five rows of the dataset:")
print(data.head())

print("\nSize of the dataset:", data.size)

print("\nNumber of missing values in each column:")
print(data.isnull().sum())

print("\nSum of numerical columns:")
print(data.sum(numeric_only=True))

print("\nAverage of numerical columns:")
print(data.mean(numeric_only=True))

print("\nMinimum values of numerical columns:")
print(data.min(numeric_only=True))

print("\nMaximum values of numerical columns:")
print(data.max(numeric_only=True))

data.to_csv('exported_data.csv', index=False)
