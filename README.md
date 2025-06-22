# 📖 Prompt to Plot: AI Story Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Built with-Streamlit-ff4b4b.svg)](https://streamlit.io/)
[![Hugging Face Model](https://img.shields.io/badge/Model-Zephyr-7B-yellow)](https://huggingface.co/HuggingFaceH4/zephyr-7b-alpha)

---

## Table of Contents
- [Demo](#demo)
- [Overview](#overview)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Deployment on Streamlit](#deployment-on-streamlit)
- [Directory Tree](#directory-tree)
- [Bug / Feature Request](#bug--feature-request)
- [Future Scope](#future-scope)
- [License](#license)
- [Author](#author)

---

## Demo

> 💻 Live Demo: [Click here to try it!](https://prompt-to-plot-ztgfmvglzhmkxv7qwztc4g.streamlit.app/)

### UI Preview:

**Prompt & Genre Input**  
![Prompt Input](screenshots/input.png)

**Generated Story Output**  
![Story Output](screenshots/output.png)

---

## Overview

**Prompt to Plot** is a Streamlit-based AI storytelling app that transforms your ideas into creative narratives using the [Zephyr-7B](https://huggingface.co/HuggingFaceH4/zephyr-7b-alpha) language model.

This project is ideal for:
- Writers looking for inspiration  
- NLP learners and students  
- Educators teaching AI-generated content  
- Anyone who loves imaginative storytelling

### 🧩 Key Features:
- Prompt input from user  
- Genre selection (Horror, Sci-Fi, Romance, etc.)  
- Adjustable story length (Short / Medium / Long)  
- Generates creative stories using Hugging Face API  
- Download generated story as `.txt`

---

## Installation

> Requires **Python 3.11**

### 1. Clone the Repository

```bash
git clone https://github.com/ANUSHKA49282/prompt-to-plot.git
cd prompt-to-plot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Hugging Face API Key

Create a file named `.env` in the root folder:

```env
HF_API_KEY=your_huggingface_token_here
```

> Create a free token from: https://huggingface.co/settings/tokens  
> Use “Read” access level

---

## How to Use

```bash
python -m streamlit run app.py
```

1. Enter your story prompt  
2. Choose a genre and length  
3. Click **Generate Story ✨**  
4. Read and download your AI-generated story!

---

## Deployment on Streamlit

To deploy your app on [streamlit.io/cloud](https://streamlit.io/cloud):

1. Sign in with GitHub  
2. Create a new app using this repo: `ANUSHKA49282/prompt-to-plot`  
3. Set `app.py` as the main file  
4. In **Advanced settings → Secrets**, add:

```env
HF_API_KEY=your_token_here
```

5. Click **Deploy**

---

## Directory Tree

```text
prompt-to-plot/
├── app.py
├── .env              # (ignored from GitHub)
├── LICENSE
├── README.md
├── requirements.txt
├── .gitignore
└── screenshots/
    ├── input.png
    └── output.png
```

---

## Bug / Feature Request

Found a bug or want a new feature?  
Open an issue here:  
👉 https://github.com/ANUSHKA49282/prompt-to-plot/issues

---

## Future Scope

1. **Genre-Based Prompt Suggestions**  
   Auto-fill example prompts based on selected genre

2. **Voice Narration**  
   Add text-to-speech for the generated story

3. **User Login & Saved Stories**  
   Allow users to save and revisit past stories

4. **Live Deployment**  
   Host the app on Streamlit Cloud with 24/7 access

5. **Multi-language Support**  
   Generate stories in other languages like Hindi, Telugu, etc.

---

## License

Distributed under the MIT License.  
See [LICENSE](LICENSE) for more details.

---

## Author

**Anushka**  
B.Tech Student, VIT AP University  
GitHub: [ANUSHKA49282](https://github.com/ANUSHKA49282)
