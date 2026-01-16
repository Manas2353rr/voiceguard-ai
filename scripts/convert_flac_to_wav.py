import soundfile as sf
import os

# Path where LibriSpeech test-clean is extracted
INPUT_DIR = "test-clean"
OUTPUT_DIR = "data/real"

os.makedirs(OUTPUT_DIR, exist_ok=True)

count = 0

for root, _, files in os.walk(INPUT_DIR):
    for file in files:
        if file.endswith(".flac"):
            flac_path = os.path.join(root, file)
            wav_path = os.path.join(OUTPUT_DIR, f"real_{count}.wav")

            audio, sr = sf.read(flac_path)
            sf.write(wav_path, audio, sr)

            count += 1
            if count == 10:   # only convert 10 files
                break
    if count == 10:
        break

print(f"✅ Converted {count} real voice files")
