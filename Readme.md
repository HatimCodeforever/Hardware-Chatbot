# 🔗 Hardware Chatbot-Chainlit + Google Gemini Project

This project integrates [Chainlit](https://docs.chainlit.io) with **Google Gemini** to build an interactive chatbot or AI-powered application.

---

## 📦 Requirements

- Python 3.9+
- A Google Gemini API Key ([Get it here](https://makersuite.google.com/app/apikey))
- `virtualenv` (recommended)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/chainlit-gemini-project.git
cd chainlit-gemini-project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install packages manually and generate it:

```bash
pip install chainlit google-generativeai python-dotenv
pip freeze > requirements.txt
```

---

## 🔐 Set Up Environment Variable

### Option 1: Use `.env` File

Create a file named `.env` in the root folder and add:

```env
GEMINI_KEY=your_google_gemini_api_key_here
```

## 🚀 Run the Project

```bash
chainlit run main.py
```
