# 🎓 College Helpdesk Chatbot

An intelligent chatbot built using **Natural Language Processing (NLP)** and **Machine Learning** to assist students with college-related queries such as admission, fees, courses, routines, notices, and more.

---

## 🚀 Features

* 💬 Intent-based chatbot using Machine Learning
* 🌐 Web interface built with Flask
* 📄 Direct PDF access for fee structure
* 📚 Covers multiple intents:

  * Admission
  * Fees
  * Courses
  * Class Routine
  * Exam Routine
  * Notices
  * Student Login
  * Anti-Ragging Policy
  * Contact Information
* ⚡ Fast and responsive UI
* 🎯 Confidence-based fallback system

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **Scikit-learn (Logistic Regression, TF-IDF)**
* **HTML, CSS, JavaScript**
* **Git & GitHub**

---

## 📂 Project Structure

```bash
College-Chatbot/
│
├── app.py               # Main Flask app
├── model.py             # NLP model (intent classification)
├── intents.json         # Training data (intents)
├── requirements.txt     # Dependencies
├── .gitignore           # Ignored files
│
├── templates/
│   └── index.html       # Chatbot UI
│
└── document_loaders/
    └── BTech_2025_2026.pdf
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Farhan-q18/College-Chatbot.git
cd College-Chatbot
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

*(or if using uv)*

```bash
uv pip install -r requirements.txt
```

---

### 3. Run the application

```bash
python app.py
```

*(or)*

```bash
uv run python app.py
```

---

### 4. Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

1. User enters a query in the chatbot UI
2. Input is processed using **TF-IDF Vectorizer**
3. A **Logistic Regression model** predicts the intent
4. The chatbot returns the most relevant response
5. If confidence is low, a fallback message is shown

---

## 🔐 Environment Variables

This project uses environment variables for security.

Create a `.env` file:

```
HF_TOKEN=your_token_here
```

⚠️ Do NOT upload `.env` to GitHub

---

## 👥 Contributors

* Farhan Qamar


---

## 📌 Future Improvements

* Will Add RAG-based document search
* Improve NLP accuracy
* will Add voice input
* Deploy on cloud (Render / Railway / AWS / vercel)

---


