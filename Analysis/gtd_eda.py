# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure seaborn settings
sns.set(style="whitegrid")

# Load the dataset
df = pd.read_csv('Data\gtd_cleaned.csv', parse_dates=['date'])
