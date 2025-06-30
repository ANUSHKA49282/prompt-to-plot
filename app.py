import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# Streamlit UI setup
st.set_page_config(page_title="Prompt to Plot", page_icon="📖")
st.title("📖 Prompt to Plot: Your Instant Story Buddy")

# User inputs
prompt = st.text_area("Enter your story prompt:", placeholder="e.g., A lonely astronaut discovers a mysterious planet...")
genre = st.selectbox("Select a genre:", ["Any", "Horror", "Romance", "Sci-Fi", "Fantasy", "Mystery"])
length = st.selectbox("Select story length:", ["Short", "Medium", "Long"])
length_tokens = {"Short": 300, "Medium": 600, "Long": 1000}
target_tokens = length_tokens[length]

# Disable button if no prompt
generate_disabled = len(prompt.strip()) == 0

if st.button("Generate Story ✨", disabled=generate_disabled):
    full_prompt = f"Write a {length.lower()} {genre.lower()} story based on this prompt: {prompt}" if genre != "Any" else f"Write a {length.lower()} story based on this prompt: {prompt}"
    
    with st.spinner("Generating your story..."):
        response = model.generate_content(full_prompt)
        story = response.text.strip()

    st.subheader("📜 Your Generated Story:")
    st.write(story)

    st.caption(f"🔢 Estimated token usage: ~{len(story.split())} tokens")

    st.download_button(
        label="📥 Download Story as .txt",
        data=story,
        file_name="my_story.txt",
        mime="text/plain"
    )
