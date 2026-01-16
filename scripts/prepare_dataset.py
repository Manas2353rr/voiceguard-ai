import os
import numpy as np
from scripts.feature_extraction import extract_features

# Get absolute path of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

REAL_PATH = os.path.join(BASE_DIR, "..", "data", "real")
FAKE_PATH = os.path.join(BASE_DIR, "..", "data", "fake")

def load_dataset():
    X = []
    y = []

    # REAL voices → label 0
    for file in os.listdir(REAL_PATH):
        if file.lower().endswith(".wav"):
            path = os.path.join(REAL_PATH, file)
            X.append(extract_features(path))
            y.append(0)

    # FAKE voices → label 1
    for file in os.listdir(FAKE_PATH):
        if file.lower().endswith(".wav"):
            path = os.path.join(FAKE_PATH, file)
            X.append(extract_features(path))
            y.append(1)

    return np.array(X), np.array(y)

if __name__ == "__main__":
    X, y = load_dataset()
    print("Samples:", len(X))
    print("Feature shape:", X.shape)
