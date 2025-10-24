
# 🧠 TUBS Visual Assistant

TUBS Visual Assistant is an open-source **AI-powered visual assistant** built with **Python Flask** and **HTML/JavaScript**.  
It uses your **device camera** to capture images and sends them — along with a **user prompt** — to **Google Gemini**, which returns intelligent, natural-language descriptions or answers about the image.

This tool is designed to assist visually impaired users or anyone who wants quick, spoken feedback about what their camera sees.

---

## 🚀 Features

- 📸 Capture real-time images from your device camera  
- 💬 Ask contextual questions or give prompts about the scene  
- 🤖 AI analysis powered by **Google Gemini**  
- 🔊 Text-to-Speech output — the assistant speaks the response aloud  
- 🪶 Lightweight Flask backend and simple frontend  
- 💻 Works directly in your browser — no special installation needed beyond Python dependencies  

---

## 🧩 Tech Stack

| Layer | Technology |
|--------|-------------|
| **Backend** | Python, Flask |
| **Frontend** | HTML, CSS, JavaScript |
| **AI Model** | Google Gemini API |
| **Speech** | Web Speech API (Text-to-Speech) |
| **Deployment** | Render / Localhost / Any Flask-compatible platform |

---

## 🏗️ Project Structure

```
tubs-visual-assistant/
│
├── app.py                     # Flask backend server
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
└── templates/
    └── index.html              # Frontend (camera + UI)
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/IDA-TUBS/TUBS-visual-assistant.gi
cd TUBS-visual-assistant
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Your Gemini API Key
Open **app.py** and set your API key directly in this line:
```python
API_KEY = "your_gemini_api_key_here"
```

### 5. Run the Application
```bash
python app.py
```

Then open your browser and visit:
```
http://127.0.0.1:8000/
```

---

## 🖥️ How It Works

1. **Camera Access**: The web app activates your device camera in fullscreen.  
2. **User Prompt**: You type a question or instruction (e.g., “What object is in front of me?”).  
3. **Capture Frame**: The app takes a snapshot from the live video feed.  
4. **AI Analysis**: The image and prompt are sent to the Gemini API.  
5. **Response & Voice**: The assistant returns a short text description and speaks it aloud using Text-to-Speech.

---

## 🧠 Example Usage

- “What text is in this image?”  
- “Describe the scene.”  
- “Is there a person or object in view?”  

---

## 🧾 License

This project is released under the **MIT License** — feel free to use and modify it freely.
