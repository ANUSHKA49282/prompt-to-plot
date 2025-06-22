import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load Hugging Face token from .env
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

# Connect to Hugging Face model
client = InferenceClient("HuggingFaceH4/zephyr-7b-alpha", token=HF_API_KEY)

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

# Story generation function
def generate_story(prompt, max_tokens):
    try:
        genre_prompt = f"Write a {genre.lower()} story." if genre != "Any" else "Write a creative story."

        response = client.chat_completion(
            messages=[
                {"role": "system", "content": genre_prompt},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.8
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Generate story button
if st.button("Generate Story ✨"):
    if not prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Crafting your story..."):
            story = generate_story(prompt, max_tokens)
            st.success("Here's your story:")
            st.write(story)
            st.download_button("📥 Download Story", data=story, file_name="story.txt", mime="text/plain")
