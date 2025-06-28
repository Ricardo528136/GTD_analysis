# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure seaborn settings
sns.set(style="whitegrid")

# Load the dataset
df = pd.read_csv('Data\gtd_cleaned.csv', parse_dates=['date'])

# Basic information about the dataset
print('Dataset shape:', df.shape)
print(df.describe())
print(df['country'].value_counts().head(10))
print(df['group_name'].value_counts().head(10))

# Plotting the number of attacks per year
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='year', order=sorted(df['year'].unique()), palette='viridis')
plt.title('Number of Attacks per Year')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Plots/attacks_per_year.png')
plt.show()