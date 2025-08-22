import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load data
df = pd.read_csv('Students Social Media Addiction.csv')

# Inspect unique values
print("Relationship Status unique values:", df['Relationship_Status'].unique())

# ✅ Map Relationship_Status to numeric score
relationship_map = {
    'Single': 2,
    'In Relationship': 1,
    'Complicated': 3
}
df['Relationship_Score'] = df['Relationship_Status'].map(relationship_map)

# ✅ Create AddictionScore BEFORE encoding
df['AddictionScore'] = (
    df['Avg_Daily_Usage_Hours'] * 0.5 +
    df['Relationship_Score'] * 0.3 +
    df['Sleep_Hours_Per_Night'] * 0.2
)

# Normalize score to 1–10
df['AddictionScore'] = 1 + 9 * (
    (df['AddictionScore'] - df['AddictionScore'].min()) /
    (df['AddictionScore'].max() - df['AddictionScore'].min())
)

# ✅ One-hot encode Relationship_Status for model input
df = pd.get_dummies(df, columns=['Relationship_Status'], prefix='RelStatus', drop_first=True)

# Encode other categorical columns (if any)
for col in df.select_dtypes(include='object').columns:
    df[col] = LabelEncoder().fit_transform(df[col])

# ✅ Define features — use one-hot columns, NOT the original one
feature_cols = [
    'Age',
    'Avg_Daily_Usage_Hours',
    'Relationship_Score',
    'Mental_Health_Score',
    'Sleep_Hours_Per_Night'
] + [c for c in df.columns if c.startswith('RelStatus_')]

X = df[feature_cols]
y = df['AddictionScore']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Evaluate
mae = abs(model.predict(X_test) - y_test).mean()
r2 = model.score(X_test, y_test)
print(f"MAE: {mae:.2f}, R2: {r2:.2f}")

# Save model
# os.makedirs('../models', exist_ok=True)
joblib.dump(model, 'addiction_model.pkl')
print("Model saved.")

model_path = os.path.abspath('.addiction_model.pkl')
print(f"Model file saved at: {model_path}")

