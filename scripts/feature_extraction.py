import librosa
import numpy as np

def extract_features(file_path):
    """
    Extract audio features for deepfake voice detection
    """
    y, sr = librosa.load(file_path, sr=None)

    # 1. MFCCs
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)
    mfcc_mean = np.mean(mfcc.T, axis=0)

    # 2. Delta MFCC
    delta_mfcc = librosa.feature.delta(mfcc)
    delta_mfcc_mean = np.mean(delta_mfcc.T, axis=0)

    # 3. Zero Crossing Rate
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))

    # 4. Spectral Centroid
    spectral_centroid = np.mean(
        librosa.feature.spectral_centroid(y=y, sr=sr)
    )

    # Combine all features
    features = np.hstack([
        mfcc_mean,
        delta_mfcc_mean,
        zcr,
        spectral_centroid
    ])

    return features

