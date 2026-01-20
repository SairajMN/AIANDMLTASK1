import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import numpy as np

# Load data
df = pd.read_csv("ai_demo.csv")
target_column = "Company"

# Features: Technology, Description, Year Introduced
features = ['Technology', 'Description', 'Year Introduced']
X = df[features]
y = df[target_column]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ('tech_year', OneHotEncoder(handle_unknown='ignore'), ['Technology', 'Year Introduced']),
        ('desc', TfidfVectorizer(max_features=100), 'Description')
    ]
)

# Model pipeline
model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Since small dataset, use cross-validation with fewer folds
scores = cross_val_score(model, X, y, cv=2, scoring='accuracy')
print(f"Cross-validation accuracy: {scores.mean():.2f} ± {scores.std():.2f}")

# Train on full data for demo
model.fit(X, y)

# Predictions on training data (not ideal, but for demo)
y_pred = model.predict(X)
print(f"Training accuracy: {accuracy_score(y, y_pred):.2f}")
print("Classification report:")
print(classification_report(y, y_pred, zero_division=0))

# Feature importance (approximate for RandomForest)
# Get feature names
ohe_features = model.named_steps['preprocessor'].named_transformers_['tech_year'].get_feature_names_out(['Technology', 'Year Introduced'])
tfidf_features = model.named_steps['preprocessor'].named_transformers_['desc'].get_feature_names_out()
all_features = np.concatenate([ohe_features, tfidf_features])

importances = model.named_steps['classifier'].feature_importances_
top_indices = np.argsort(importances)[-10:][::-1]
print("Top 10 feature importances:")
for i in top_indices:
    print(f"{all_features[i]}: {importances[i]:.4f}")
