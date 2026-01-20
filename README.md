# AIANDMLTASK1

This project performs exploratory data analysis (EDA) and basic machine learning modeling on an AI technologies dataset (`ai_demo.csv`). The analysis includes data loading, feature classification, statistical summaries, data quality assessment, and model training.

## Tasks Completed

1. **Load the dataset using Pandas and display first and last few records to understand the structure of rows and columns.**
   - Dataset loaded from `ai_demo.csv`.
   - First and last 5 rows displayed to show column structure and sample data.

2. **Identify numerical, categorical, ordinal, and binary features manually by inspecting column names and values.**
   - All features are categorical (object dtype): Technology, Description, Year Introduced, Company.
   - No numerical, ordinal, or binary features identified.

3. **Use df.info() and df.describe() to understand data types, null values, and statistical summaries.**
   - `df.info()`: 10 entries, 4 columns, all object, no null values, low memory usage.
   - `df.describe()`: Unique counts, top values, frequencies for categoricals.

4. **Check unique values in categorical columns to understand data distribution.**
   - Year Introduced: 8 unique values (e.g., 2010s x2, others x1).
   - Company: 9 unique values (General x2, others x1).
   - Technology and Description: 10 unique each.

5. **Identify target variable and input features for ML suitability.**
   - Target: Company (multi-class classification, 9 classes).
   - Features: Technology, Description, Year Introduced.
   - Suitable for classification; small dataset limits performance.

6. **Analyze dataset size and discuss whether it is suitable for machine learning.**
   - Dataset: 10 rows, 4 columns.
   - Too small for deep learning; suitable for classical ML like Random Forest, but overfitting risk high.

7. **Write clear observations about data quality issues like missing values or imbalance.**
   - No missing values.
   - No duplicates.
   - Mild imbalance in target (ratio 2.0).
   - High-cardinality in text features.
   - Overall high quality, but small size is main issue.

## Files

- `ai_demo.csv`: Dataset file.
- `eda_report.docx`: Detailed EDA report in Word format.
- `load_and_preview.py`: Script for loading and previewing data.
- `eda_report.py`: Script for EDA analysis.
- `generate_report_docx.py`: Script to generate the DOCX report.
- `modeling.py`: Script for preprocessing and modeling.
- `column_summary.csv`: Summary of columns from EDA.

## Usage

1. Run `python eda_report.py` to perform EDA and print summaries.
2. Run `python generate_report_docx.py` to generate `eda_report.docx`.
3. Run `python modeling.py` to train a model and evaluate.

## Dependencies

- pandas
- python-docx
- scikit-learn
