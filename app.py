import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load Gemini API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# Streamlit UI setup
st.set_page_config(page_title="Prompt to Plot", page_icon="📖")
st.title("📖 Prompt to Plot: Your Instant Story Buddy")

# Prompt input
prompt = st.text_area("Enter a story prompt:", placeholder="e.g., A cat who runs a cafe for kittens...")

# Genre selection
genre = st.selectbox("Choose story genre:", ["Any", "Horror", "Romance", "Sci-Fi", "Fantasy", "Mystery"])

# Length selection
length = st.selectbox("Choose story length:", ["Short", "Medium", "Long"])
length_map = {"Short": 80, "Medium": 200, "Long": 400}
max_tokens = length_map[length]

# Generate story function using Gemini
def generate_story(prompt, max_tokens):
    try:
        genre_prompt = f"Write a {genre.lower()} story." if genre != "Any" else "Write a creative story."
        full_prompt = f"{genre_prompt}\nUser prompt: {prompt}\nLimit it to around {max_tokens} words."

        response = model.generate_content(full_prompt)
        return response.text.strip()

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Generate button
if st.button("Generate Story") and prompt:
    story = generate_story(prompt, max_tokens)
    st.markdown("### ✨ Your Story:")
    st.write(story)
