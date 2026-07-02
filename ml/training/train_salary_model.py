import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

print("Loading Dataset...")

df = pd.read_csv("../datasets/placement_data.csv")

# Create a salary column if not present
if "salary_lpa" not in df.columns:
    df["salary_lpa"] = (
        df["cgpa"] * 1.2
        + df["internships"] * 0.8
        + df["projects"] * 0.5
        + df["certifications"] * 0.4
        + df["technical_score"] * 0.05
    )

print("Dataset Loaded Successfully")

# Features

X = df[
    [
        "cgpa",
        "internships",
        "projects",
        "certifications",
        "technical_score",
        "communication_score",
        "github_score"
    ]
]

# Target

y = df["salary_lpa"]

# Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Salary Model...")

# Model

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Training Completed")

# Prediction

y_pred = model.predict(X_test)

# Evaluation

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Absolute Error:", mae)
print("R2 Score:", r2)

# Feature Importance

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print("\nFeature Importance:")
print(
    importance.sort_values(
        by="Importance",
        ascending=False
    )
)

# Save Model

joblib.dump(
    model,
    "../models/salary_model.pkl"
)

print("\nsalary_model.pkl saved successfully!")