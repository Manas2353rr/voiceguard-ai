import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load sample audio
y, sr = librosa.load(librosa.ex('trumpet'))

print("Sample Rate:", sr)
print("Audio Length:", len(y))

# Plot waveform
plt.figure(figsize=(10, 3))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.tight_layout()
plt.show()


# Create spectrogram
D = librosa.amplitude_to_db(
    np.abs(librosa.stft(y)), ref=np.max
)

plt.figure(figsize=(10, 4))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title("Spectrogram")
plt.tight_layout()
plt.show()
