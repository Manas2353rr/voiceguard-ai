import React, { useState, useRef } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [recording, setRecording] = useState(false);
  const [audioURL, setAudioURL] = useState(null);

  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  const API_URL = "https://voiceguard-ai-t9hh.onrender.com//predict"; // change later for prod

  const analyzeVoice = async () => {
    if (!file) return alert("Upload or record audio first");

    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        body: formData
      });
      const data = await res.json();
      setResult(data);
    } catch {
      alert("Backend not reachable");
    } finally {
      setLoading(false);
    }
  };

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const recorder = new MediaRecorder(stream);

    mediaRecorderRef.current = recorder;
    audioChunksRef.current = [];

    recorder.ondataavailable = (e) => audioChunksRef.current.push(e.data);

    recorder.onstop = () => {
      const blob = new Blob(audioChunksRef.current, { type: "audio/wav" });
      setAudioURL(URL.createObjectURL(blob));
      setFile(new File([blob], "recorded.wav", { type: "audio/wav" }));
    };

    recorder.start();
    setRecording(true);
  };

  const stopRecording = () => {
    mediaRecorderRef.current.stop();
    setRecording(false);
  };

  const resultColor =
    result?.prediction === "FAKE" ? "#dc2626" :
    result?.prediction === "REAL" ? "#16a34a" : "#111827";

  return (
    <div style={styles.page}>
      <div style={styles.card}>
        <h1 style={styles.title}>🎙️ VoiceGuard AI</h1>
        <p style={styles.subtitle}>Real-time Deepfake Voice Detection</p>

        <input
          type="file"
          accept=".wav"
          onChange={(e) => setFile(e.target.files[0])}
          style={styles.file}
        />

        <div style={styles.buttons}>
          {!recording ? (
            <button style={styles.btn} onClick={startRecording}>
              🎤 Start Recording
            </button>
          ) : (
            <button style={{ ...styles.btn, background: "#dc2626" }} onClick={stopRecording}>
              ⏹ Stop Recording
            </button>
          )}

          <button style={styles.analyzeBtn} onClick={analyzeVoice}>
            Analyze Voice
          </button>
        </div>

        {audioURL && (
          <audio controls src={audioURL} style={{ marginTop: 15 }} />
        )}

        {loading && <p style={styles.loading}>Analyzing voice…</p>}

        {result && (
          <div style={styles.resultBox}>
            <h2 style={{ color: resultColor, fontSize: 32 }}>
              {result.prediction}
            </h2>
            <p>Confidence: <b>{result.confidence}</b></p>
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    background: "linear-gradient(135deg, #e0f2fe, #f0fdf4)",
    fontFamily: "sans-serif"
  },
  card: {
    background: "#fff",
    padding: 40,
    borderRadius: 16,
    width: 380,
    boxShadow: "0 20px 40px rgba(0,0,0,0.1)",
    textAlign: "center"
  },
  title: { marginBottom: 5 },
  subtitle: { color: "#6b7280", marginBottom: 20 },
  file: { marginBottom: 15 },
  buttons: { display: "flex", flexDirection: "column", gap: 10 },
  btn: {
    padding: 10,
    borderRadius: 8,
    border: "none",
    background: "#2563eb",
    color: "#fff",
    cursor: "pointer"
  },
  analyzeBtn: {
    padding: 10,
    borderRadius: 8,
    border: "none",
    background: "#111827",
    color: "#fff",
    cursor: "pointer"
  },
  loading: { marginTop: 15, fontWeight: "bold" },
  resultBox: { marginTop: 20 }
};

export default App;
