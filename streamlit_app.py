import streamlit as st
import google.generativeai as genai

# 1. SETUP & APP CONFIG
st.set_page_config(page_title="AI Interview Reviewer", page_icon="🎯")
st.title("🎯 AI Interview Answer Reviewer")
st.markdown("---")

# 2. SECURE API KEY ACCESS
# Make sure you have 'GEMINI_API_KEY' in your Streamlit Secrets!
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("❌ Missing Gemini API Key! Please add it to your Streamlit Secrets.")
    st.stop()

# 3. HELPER: PLAY COMPLETION BEEP
def play_completion_beep():
    # A professional 'ding' sound to alert the user
    sound_url = "https://www.soundjay.com/buttons/beep-01a.mp3"
    st.markdown(f'<audio autoplay><source src="{sound_url}" type="audio/mp3"></audio>', unsafe_allow_html=True)

# 4. USER INPUTS
st.subheader("Step 1: The Question")
question = st.text_input("What interview question are you practicing?", placeholder="e.g., Tell me about a time you solved a difficult problem.")

st.subheader("Step 2: Your Answer")
tab1, tab2 = st.tabs(["✍️ Type Your Answer", "🎙️ Speak Your Answer"])

with tab1:
    text_answer = st.text_area("Type your response here...", height=150)

with tab2:
    # This is the 'Ear' of the app
    audio_file = st.audio_input("Record your answer (Native Gemini Audio Processing)")

# 5. THE REVIEW LOGIC
if st.button("🚀 Analyze My Answer"):
    # Check if we have a question
    if not question:
        st.warning("⚠️ Please provide an interview question first.")
    # Check if we have either a text or audio answer
    elif not text_answer and not audio_file:
        st.warning("⚠️ Please either type or record an answer.")
    else:
        with st.spinner("Gemini is analyzing your performance..."):
            try:
                model = genai.GenerativeModel('gemini-3-pro-preview')
                
                # PERSONA PROMPT
                system_instruction = f"""
                You are a professional hiring manager. 
                Question: {question}
                
                Analyze the user's provided answer. 
                If the input is audio, listen for tone, clarity, and content.
                If the input is text, focus on structure and keywords.
                
                Provide:
                1. Score: (out of 10)
                2. What's good:
                3. What's missing:
                4. How to improve: (Give a better sample answer)
                """

                # EXECUTE BASED ON INPUT TYPE
                if audio_file:
                    # Multimodal path: Audio + Text
                    response = model.generate_content([
                        system_instruction,
                        {"mime_type": "audio/wav", "data": audio_file.read()}
                    ])
                else:
                    # Text only path
                    response = model.generate_content(f"{system_instruction}\n\nUser's Text Answer: {text_answer}")

                # 6. SHOW RESULTS
                st.divider()
                st.subheader("📋 Evaluation Result")
                st.markdown(response.text)
                
                # Feedback features
                play_completion_beep()
                st.toast("Analysis Complete!", icon="✅")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")