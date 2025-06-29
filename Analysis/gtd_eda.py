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

# Plotting top 10 countries with the most attacks
plt.figure(figsize=(12, 6))
top_countries = df['country'].value_counts().head(10).index
sns.countplot(data=df[df['country'].isin(top_countries)], y='country', order=top_countries, palette='viridis')
plt.title('Top 10 Countries with the Most Attacks')
plt.xlabel('Number of Attacks')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('Plots/top_countries_attacks.png')
plt.show()

# Plotting regions with the most attacks
plt.figure(figsize=(12, 6))
sns.countplot(data=df, y='region', order=df['region'].value_counts().index, palette='viridis')
plt.title('Regions with the Most Attacks')
plt.xlabel('Number of Attacks')
plt.ylabel('Region')
plt.tight_layout()
plt.savefig('Plots/regions_attacks.png')
plt.show()

# Plotting casualties over the years
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='year', y='casualties', estimator='sum', marker='o', color='red')
plt.title('Total Casualties Over the Years')
plt.xlabel('Year')
plt.ylabel('Casualties')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Plots/casualties_over_years.png')
plt.show()

# Plotting the distribution of attack types
plt.figure(figsize=(12, 6))
sns.countplot(data=df, y='attack_type', order=df['attack_type'].value_counts().index, palette='viridis')
plt.title('Distribution of Attack Types')
plt.xlabel('Number of Attacks')
plt.ylabel('Attack Type')
plt.tight_layout()
plt.savefig('Plots/attack_types_distribution.png')
plt.show()

# Plotting the weapons used in attacks
plt.figure(figsize=(12, 6))
sns.countplot(data=df, y='weapon_type', order=df['weapon_type'].value_counts().index, palette='cubehelix')
plt.title('Weapons Used in Attacks')
plt.xlabel('Number of Attacks')
plt.ylabel('Weapon Type')
plt.tight_layout()
plt.savefig('Plots/weapons_used_in_attacks.png')
plt.show()

# Plotting the relationship between casualties and attack type
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='attack_type', y='casualties', palette='viridis')
plt.title('Casualties by Attack Type')
plt.xlabel('Attack Type')
plt.ylabel('Casualties')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Plots/casualties_by_attack_type.png')
plt.show()

# Plotting the relationship between casualties and region
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='region', y='casualties', palette='viridis')
plt.title('Casualties by Region')
plt.xlabel('Region')
plt.ylabel('Casualties')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Plots/casualties_by_region.png')
plt.show()

# Plotting the deadliest groups
plt.figure(figsize=(12, 6))
top_groups = df['group_name'].value_counts().head(10).index
sns.barplot(data=df[df['group_name'].isin(top_groups)], y='group_name', x='casualties', estimator='sum', order=top_groups, palette='viridis')
plt.title('Deadliest Groups by Casualties')
plt.xlabel('Total Casualties')
plt.ylabel('Group Name')
plt.tight_layout()
plt.savefig('Plots/deadliest_groups.png')
plt.show()