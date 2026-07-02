import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print("Loading Skills Dataset...")

df = pd.read_csv("../datasets/skills_data.csv")

print("Dataset Loaded Successfully")

# Convert text columns to numeric

label_skill = LabelEncoder()
label_category = LabelEncoder()
label_demand = LabelEncoder()

df["skill"] = label_skill.fit_transform(df["skill"])
df["category"] = label_category.fit_transform(df["category"])
df["demand_level"] = label_demand.fit_transform(df["demand_level"])

# Features

X = df[
    [
        "category",
        "average_salary_lpa",
        "interview_frequency"
    ]
]

# Target

y = df["skill"]

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Skill Model...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Training Completed")

# Prediction

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

# Save Model

joblib.dump(
    model,
    "../models/skill_model.pkl"
)

joblib.dump(
    label_skill,
    "../models/skill_encoder.pkl"
)

joblib.dump(
    label_category,
    "../models/category_encoder.pkl"
)

print("\nskill_model.pkl saved successfully!")