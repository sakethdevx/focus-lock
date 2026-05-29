# 🧠 Focus-Lock: Cognitive Telemetry Engine

**Domain:** Mental Health (Developer Well-being)  
**Built for:** Google "Build with Gemma" Buildathon  

## 🛑 The Problem
Developers experience intense cognitive burnout and executive dysfunction loops (e.g., hyper-fragmented window switching, compilation error spirals). By the time physical symptoms like headaches manifest, the cognitive crash has already happened. Furthermore, corporate developers cannot use cloud-based AI mental health tools because streaming active workspace telemetry to a third-party server is a massive security and IP violation.

## 💡 The Solution
**Focus-Lock** is a pure-software digital phenotyping engine. It simulates tracking behavioral telemetry—window switching velocity, typing jitter, and syntax error rates—to calculate a real-time "Cognitive Fatigue Score." 

When an executive dysfunction loop is detected, the system intercepts the behavior and triggers an immediate, contextual lockdown protocol. Powered by **Gemma 4 running locally via LM Studio**, it guarantees **absolute offline data privacy** with zero-latency inference.

---

## ✨ Core Features
* **Edge AI Inference:** Uses a local Gemma 4 model via an OpenAI-compatible gateway. No cloud APIs, no data harvesting.
* **Behavioral Telemetry Matrix:** Simulates active tracking of developer friction metrics rather than relying on manual mood-logging.
* **Deterministic JSON Structuring:** The backend utilizes strict prompting to force the LLM to output predictable, heavily structured JSON payloads for the frontend to render.
* **Spatial UI Architecture:** A minimalist, high-contrast, geometric interface featuring glassmorphism, neon-blue accents, and fluid keyframe animations to simulate a native OS-level interceptor.

---

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **AI / Inference:** Gemma 4 (Local GGUF), LM Studio, OpenAI Python SDK
* **Frontend:** HTML5, CSS3 (Spatial Design System), Vanilla JavaScript
* **Networking:** Ngrok (for secure HTTPS tunneling to mobile devices)

---

## 🚀 Quick Start Guide

### 1. Initialize the Local AI Model
1. Download and install [LM Studio](https://lmstudio.ai/).
2. Load your **Gemma 4** model.
3. Start the Local Server on port `1234` (ensure it binds to `127.0.0.1`).

### 2. Setup the Python Backend
Ensure you have Python 3.8+ installed.

```bash
# Clone the repository
git clone https://github.com/sakethdevx/focus-lock.git
cd focus-lock

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn openai jinja2

### 3. Run the Backend Server
Start the Uvicorn development server:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

Once running, access the Focus-Lock Core dashboard in your web browser at:
`http://localhost:8000`
```,StartLine:51,TargetContent: