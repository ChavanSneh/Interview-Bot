# 🎯 AI Interview Answer Reviewer

A professional tool designed to help candidates perfect their interview responses. This application uses **OpenAI's GPT-4o** to analyze answers and **Whisper** to transcribe voice responses, providing structured feedback and scoring.

## 🚀 Live Demo
[Link to your Streamlit App (e.g., https://your-app.streamlit.app)]

## ✨ Key Features
* **Dual-Mode Input:** Users can either type their responses or speak them directly via microphone.
* **Speech-to-Text Integration:** Uses OpenAI's `whisper-1` model for high-accuracy voice transcription.
* **Structured AI Evaluation:** Provides a 1-10 score, highlights strengths, identifies missing points, and suggests specific improvements.
* **Audible Feedback:** Features an automated audio notification (Beep) upon completion of the review.

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/) (Python-based web framework)
* **AI Engine:** OpenAI GPT-4o (for evaluation logic)
* **Voice Processing:** OpenAI Whisper (for speech-to-text)
* **Security:** Streamlit Secrets Management (for API key protection)

## ⚙️ Local Setup
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
   "your_openai_api_key_here"
   ```


4. Run the app

   ```
   streamlit run streamlit_app.py
   ```
