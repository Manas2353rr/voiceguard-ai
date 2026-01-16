import librosa
import librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.load(librosa.ex("trumpet"))

mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20)

plt.figure(figsize=(10, 4))
librosa.display.specshow(mfcc, x_axis='time')
plt.colorbar()
plt.title("MFCC Features")
plt.tight_layout()
plt.show()
