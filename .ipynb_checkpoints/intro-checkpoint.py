import pandas as pd

df = pd.read_csv(r'C:\Users\Lenovo\Desktop\DS Assignment\online_gaming_behavior_dataset.csv')

print("\n\nDescriptive Statistics for Numerical Columns:")
print(df.describe().to_markdown(numalign="left", stralign="left"))

print("\n---------------------------------------------------------------")

print("\n\nAnalysis of Categorical Columns:")

categorical_cols = ['Gender', 'Location', 'GameGenre', 'GameDifficulty', 'EngagementLevel']

for col in categorical_cols:
    print(f"\n--- Column: {col} ---")
    print(df[col].value_counts().to_markdown(numalign="left", stralign="left"))
    print(f"Unique values: {df[col].nunique()}")