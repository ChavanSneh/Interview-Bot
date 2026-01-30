# 🎯 AI Interview Answer Reviewer (Multimodal Edition)

A sophisticated interview preparation tool built with **Streamlit** and **Google Gemini 1.5 Flash**. This application allows users to practice interview questions through either text or voice, providing instant, high-fidelity feedback using native multimodal AI processing.

## 🚀 Live Demo
[Insert your Streamlit Cloud Link Here]

## ✨ Key Features
* **Multimodal Input:** Native support for both text-based responses and direct audio recordings.
* **Direct Audio Intelligence:** Unlike traditional pipelines that require a separate Speech-to-Text model (like Whisper), this app leverages **Gemini 1.5 Flash's native audio-processing** capabilities to analyze tone and content directly.
* **Expert Personas:** The AI is prompted as a professional Hiring Manager to provide realistic scoring and critique.
* **Automated Feedback Loop:** Provides a structured 4-point evaluation:
    1. Numerical Score (1-10)
    2. Strengths Analysis
    3. Gap Identification
    4. "Model Answer" Suggestions
* **Audible Alerts:** Integrated browser-based audio notifications to signal task completion.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **AI Engine:** Google Generative AI (Gemini 1.5 Flash)
* **Environment:** Python 3.9+
* **Security:** Streamlit Secrets Management (`secrets.toml`)

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/chavansneh/ai-interview-reviewer.git](https://github.com/chavansneh/ai-interview-reviewer.git)
   cd ai-interview-reviewer

### How to run it on your own machine

2. Install the requirements

   ```
   pip install -r requirements.txt
   ```

3. Configure Secrets:
   Ceate a folder .streamlit/ and a file called secrets.toml inside it

   ```
   GEMINI_API_KEY =
   "your_gemini_api_key_here"
   ```


4. Run the app

   ```
   streamlit run streamlit_app.py
   ```
