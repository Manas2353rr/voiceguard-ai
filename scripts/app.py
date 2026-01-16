from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import joblib
import numpy as np


from scripts.feature_extraction import extract_features


app = FastAPI(title="VoiceGuard AI")

# Allow frontend access later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Absolute paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "voiceguard_model.pkl")

# Load trained model
model = joblib.load(MODEL_PATH)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    temp_audio = os.path.join(BASE_DIR, "temp.wav")

    # Save uploaded audio
    with open(temp_audio, "wb") as f:
        f.write(await file.read())

    # Extract features
    features = extract_features(temp_audio)
    features = np.expand_dims(features, axis=0)

    # Predict
    prediction = model.predict(features)[0]
    confidence = max(model.predict_proba(features)[0])

    label = "FAKE" if prediction == 1 else "REAL"

    return {
        "prediction": label,
        "confidence": round(float(confidence), 2)
    }
