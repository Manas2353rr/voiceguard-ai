# 🎙️ VoiceGuard AI

**Real-time Deepfake Voice Detection System**

VoiceGuard AI is a machine learning-powered web application that detects deepfake and synthetic voice recordings in real-time. Built with FastAPI and React, it uses advanced audio feature extraction and Random Forest classification to distinguish between authentic and AI-generated voices.

---

## ✨ Features

- 🎤 **Real-time Audio Recording** - Record audio directly in your browser
- 📁 **File Upload** - Upload WAV audio files for analysis
- 🤖 **ML-Powered Detection** - Advanced machine learning model for accurate detection
- 📊 **Confidence Scores** - Get detailed confidence metrics for each prediction
- 🎨 **Modern UI** - Clean, responsive user interface
- ⚡ **Fast API** - Lightning-fast backend powered by FastAPI
- 🌐 **Cloud Deployed** - Ready-to-use deployed backend

---

## 🏗️ Architecture

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│   React Frontend │ ──────► │  FastAPI Backend │ ──────► │  ML Model (RF)  │
│   (Port 3000)    │         │   (Port 10000)   │         │  (Pickle File)  │
└─────────────────┘         └──────────────────┘         └─────────────────┘
         │                            │
         │                            │
    Audio Input                  Feature Extraction
    (Record/Upload)              (MFCC, ZCR, etc.)
```

### Components

1. **Frontend (React)**: User interface for recording/uploading audio and displaying results
2. **Backend (FastAPI)**: REST API that processes audio files and returns predictions
3. **ML Model**: Pre-trained Random Forest classifier for voice authenticity detection

---

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Librosa** - Audio feature extraction
- **Scikit-learn** - Machine learning model
- **NumPy** - Numerical computations
- **Joblib** - Model serialization

### Frontend
- **React 19.2.3** - UI framework
- **React Scripts** - Build tooling
- **MediaRecorder API** - Browser audio recording

### Machine Learning
- **Random Forest Classifier** - 200 estimators
- **Audio Features**: MFCC, Delta MFCC, Zero Crossing Rate, Spectral Centroid

---

## 📋 Prerequisites

- **Python 3.8+**
- **Node.js 14+** and **npm**
- **Audio files** in WAV format

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd "VoiceGaurd AI"
```

### 2. Backend Setup

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
cd voiceguard-ui
npm install
```

---

## 🎯 Usage

### Running the Backend

```bash
# From project root
uvicorn scripts.app:app --host 0.0.0.0 --port 10000 --reload
```

The API will be available at `http://localhost:10000`

### Running the Frontend

```bash
# From voiceguard-ui directory
cd voiceguard-ui
npm start
```

The frontend will be available at `http://localhost:3000`

### Using the Application

1. **Record Audio**: Click "🎤 Start Recording" to record audio directly in your browser
2. **Upload Audio**: Click "Choose File" to upload a WAV audio file
3. **Analyze**: Click "Analyze Voice" to get the prediction
4. **View Results**: See the prediction (REAL/FAKE) with confidence score

---

## 📡 API Documentation

### Endpoint: `POST /predict`

Analyzes an audio file and returns a prediction.

**Request:**
- **Method**: POST
- **Content-Type**: multipart/form-data
- **Body**: 
  - `file`: Audio file (WAV format)

**Response:**
```json
{
  "prediction": "REAL" | "FAKE",
  "confidence": 0.95
}
```

**Example using cURL:**
```bash
curl -X POST "http://localhost:10000/predict" \
  -F "file=@audio_sample.wav"
```

**Example using Python:**
```python
import requests

url = "http://localhost:10000/predict"
files = {"file": open("audio_sample.wav", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

---

## 🧠 Model Training

### Preparing the Dataset

1. Organize your audio files:
   ```
   data/
   ├── real/    # Authentic voice samples (.wav)
   └── fake/    # Deepfake/synthetic voice samples (.wav)
   ```

2. Convert FLAC to WAV (if needed):
   ```bash
   python scripts/convert_flac_to_wav.py
   ```

### Training the Model

```bash
python scripts/train_model.py
```

This will:
- Load audio files from `data/real/` and `data/fake/`
- Extract features from each file
- Train a Random Forest classifier
- Evaluate the model and save it to `models/voiceguard_model.pkl`

### Feature Extraction

The model uses the following audio features:
- **MFCC (20 coefficients)**: Mel-frequency cepstral coefficients
- **Delta MFCC**: First-order derivatives of MFCC
- **Zero Crossing Rate**: Rate of sign changes in audio signal
- **Spectral Centroid**: Center of mass of the spectrum

---

## 📁 Project Structure

```
VoiceGuard AI/
├── scripts/
│   ├── app.py                    # FastAPI backend server
│   ├── feature_extraction.py     # Audio feature extraction
│   ├── train_model.py            # Model training script
│   ├── prepare_dataset.py        # Dataset loader
│   ├── convert_flac_to_wav.py   # Audio format converter
│   ├── test_audio.py            # Audio testing utilities
│   └── visualize_mfcc.py        # MFCC visualization
├── models/
│   └── voiceguard_model.pkl     # Trained model (pre-trained)
├── voiceguard-ui/               # React frontend
│   ├── src/
│   │   ├── App.js               # Main React component
│   │   ├── App.css              # Component styles
│   │   └── index.js             # React entry point
│   ├── public/                  # Static assets
│   └── package.json             # Frontend dependencies
├── requirements.txt             # Python dependencies
├── render.yaml                  # Render deployment config
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

---

## 🚢 Deployment

### Backend Deployment (Render)

The project includes a `render.yaml` configuration for easy deployment on Render:

```yaml
services:
  - type: web
    name: voiceguard-backend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn scripts.app:app --host 0.0.0.0 --port 10000
```

**Steps:**
1. Push code to GitHub
2. Connect repository to Render
3. Render will automatically detect `render.yaml` and deploy

### Frontend Deployment

Build the React app for production:

```bash
cd voiceguard-ui
npm run build
```

Deploy the `build/` folder to any static hosting service:
- **Vercel**: `vercel --prod`
- **Netlify**: Drag and drop `build/` folder
- **GitHub Pages**: Follow React deployment guide

**Important**: Update the API URL in `voiceguard-ui/src/App.js` to point to your deployed backend.

---

## 🔧 Configuration

### Backend Configuration

- **Port**: Default 10000 (configurable in `render.yaml` or startup command)
- **CORS**: Currently allows all origins (`*`) - restrict for production
- **Model Path**: `models/voiceguard_model.pkl` (relative to `scripts/`)

### Frontend Configuration

Update the API URL in `voiceguard-ui/src/App.js`:

```javascript
const API_URL = "https://your-backend-url.com/predict";
```

---

## 🧪 Testing

### Test Audio Processing

```bash
python scripts/test_audio.py
```

### Visualize MFCC Features

```bash
python scripts/visualize_mfcc.py
```

---

## 📊 Model Performance

The Random Forest classifier is trained with:
- **Algorithm**: Random Forest
- **Estimators**: 200 trees
- **Train/Test Split**: 80/20
- **Stratified**: Yes (maintains class balance)

Model evaluation metrics are displayed during training.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🐛 Known Issues

- API URL in frontend has double slash (`//predict`) - should be fixed to `/predict`
- Temporary audio files are saved in `scripts/` directory - consider cleanup mechanism
- CORS is set to allow all origins - should be restricted in production

---

## 🔮 Future Enhancements

- [ ] Support for multiple audio formats (MP3, FLAC, etc.)
- [ ] Real-time streaming audio analysis
- [ ] Batch file processing
- [ ] User authentication and history
- [ ] Advanced visualization of audio features
- [ ] Model versioning and A/B testing
- [ ] Docker containerization
- [ ] CI/CD pipeline setup

---

## 📞 Support

For issues, questions, or contributions, please open an issue on GitHub.

---

## 🙏 Acknowledgments

- **Librosa** - Audio analysis library
- **Scikit-learn** - Machine learning framework
- **FastAPI** - Modern web framework
- **React** - UI framework

---

**Made with ❤️ for detecting deepfake voices**
