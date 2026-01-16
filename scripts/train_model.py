from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

from prepare_dataset import load_dataset

# Load data
X, y = load_dataset()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

# Save model safely
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models")
os.makedirs(MODEL_DIR, exist_ok=True)

model_path = os.path.join(MODEL_DIR, "voiceguard_model.pkl")
joblib.dump(model, model_path)

print("Model saved at:", model_path)
