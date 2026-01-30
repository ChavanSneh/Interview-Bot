import streamlit as st
from openai import OpenAI

# 1. SETUP & APP NAME
st.set_page_config(page_title="AI Interview Answer Reviewer", page_icon="🎯")
st.title("🎯 AI Interview Answer Reviewer")
st.markdown("---")

# 2. SECURE API KEY ACCESS
# This looks for the key in your .streamlit/secrets.toml file or Streamlit Cloud Secrets
if "OPENAI_API_KEY" in st.secrets:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
else:
    st.error("❌ Missing API Key! Please add it to your Streamlit Secrets.")
    st.stop()

# 3. HELPER FUNCTION: THE "BEEP" ALERT
def play_completion_beep():
    # This plays a professional 'ding' sound when the review is ready
    sound_url = "https://www.soundjay.com/buttons/beep-01a.mp3"
    st.markdown(f'<audio autoplay><source src="{sound_url}" type="audio/mp3"></audio>', unsafe_allow_html=True)

# 4. USER INPUTS (Text & Voice)
st.subheader("Step 1: Provide the Question")
question = st.text_input("What is the interview question?", placeholder="e.g., Why do you want this internship?")

st.subheader("Step 2: Provide Your Answer")
tab1, tab2 = st.tabs(["✍️ Type Answer", "🎙️ Record Answer"])

with tab1:
    text_answer = st.text_area("Your Response", placeholder="Type your answer here...", height=150)

with tab2:
    # This is the 'Ear' of your app!
    audio_data = st.audio_input("Click to record your voice")
    voice_answer = ""
    if audio_data:
        with st.spinner("Transcribing your voice..."):
            transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_data)
            voice_answer = transcript.text
            st.success(f"Transcribed: {voice_answer}")

# Decide which answer to use (Voice takes priority if recorded)
final_answer = voice_answer if voice_answer else text_answer

# 5. THE AI REVIEWER LOGIC
if st.button("🚀 Review My Answer"):
    if not question or not final_answer:
        st.warning("⚠️ Please provide both a question and an answer (typed or spoken).")
    else:
        with st.spinner("Hiring Manager is analyzing..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o", 
                    messages=[
                        {"role": "system", "content": "You are a professional hiring manager. Analyze the user's interview answer. Provide: 1. Score (/10), 2. What's good, 3. What's missing, 4. How to improve."},
                        {"role": "user", "content": f"Question: {question}\nAnswer: {final_answer}"}
                    ]
                )
                
                # Show Result
                result = response.choices[0].message.content
                st.divider()
                st.subheader("📋 Evaluation Result")
                st.markdown(result)
                
                # Trigger the 'Found My Phone' style beep
                play_completion_beep()
                st.toast("Review Complete!", icon="✅")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")