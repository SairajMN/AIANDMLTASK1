import pandas as pd
import numpy as np

csv_path = "ai_demo.csv"
target_column = "Company"

# Load data
df = pd.read_csv(csv_path)

# Print head/tail
print("First 5 rows:")
print(df.head().to_string(index=False))
print("\nLast 5 rows:")
print(df.tail().to_string(index=False))

# df.info() and df.describe()
print("\ndf.info():")
df.info()
print("\ndf.describe():")
print(df.describe(include='all').to_string())

# Summarize dtype, unique counts, missing%
summary = pd.DataFrame({
    'dtype': df.dtypes,
    'unique': df.nunique(),
    'missing%': (df.isna().sum() / len(df)) * 100
})
print("\nColumn Summary:")
print(summary.to_string())

# Suggest types heuristically
def suggest_type(col):
    if df[col].dtype in ['int64', 'float64']:
        return 'numeric'
    elif df[col].nunique() == 2:
        return 'binary'
    elif df[col].nunique() < 10:
        return 'categorical'
    else:
        return 'high-cardinality'
summary['suggested_type'] = summary.index.map(suggest_type)
print("\nSuggested Types:")
print(summary[['suggested_type']].to_string())

# value_counts for categoricals
categoricals = [col for col in df.columns if df[col].dtype == 'object' or df[col].nunique() < 20]
for col in categoricals:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts().to_string())

# Target counts and proportions
print(f"\nTarget ({target_column}) counts:")
print(df[target_column].value_counts().to_string())
print(f"\nTarget proportions:")
print(df[target_column].value_counts(normalize=True).to_string())
imbalance_ratio = df[target_column].value_counts().max() / df[target_column].value_counts().min()
print(f"Imbalance ratio: {imbalance_ratio:.2f}")

# Missingness table
missing_table = df.isna().sum().reset_index()
missing_table.columns = ['column', 'missing_count']
print("\nMissingness Table:")
print(missing_table.to_string())

# Duplicates
print(f"\nDuplicate rows: {df.duplicated().sum()}")

# Correlation hints (numeric only)
numeric_cols = df.select_dtypes(include=[np.number]).columns
if len(numeric_cols) > 1:
    corr = df[numeric_cols].corr()
    print("\nCorrelation matrix:")
    print(corr.to_string())

# IQR outlier counts
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((df[col] < Q1 - 1.5 * IQR) | (df[col] > Q3 + 1.5 * IQR)).sum()
    print(f"Outliers in {col}: {outliers}")

# Save column_summary.csv
summary.to_csv('column_summary.csv')
print("\nSaved column_summary.csv")
