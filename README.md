# BankBot — Banking Q&A Chatbot

A Flask-based intelligent banking question-answering chatbot trained with a Random Forest classifier and TF-IDF vectorization. Built as part of PW Skills coursework, the project ships with full software-engineering documentation (HLD, LLD, Architecture, Wireframe, DPR).

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Setup & Running](#setup--running)
- [API Reference](#api-reference)
- [Documentation](#documentation)

---

## Overview

BankBot accepts natural-language banking questions (e.g., "How do I check my balance?", "What is the interest rate on a savings account?") and returns a predicted answer class using a pre-trained Random Forest model.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| ML Model | Scikit-learn — Random Forest Classifier |
| Text Features | TF-IDF Vectorizer |
| Label Encoding | Scikit-learn LabelEncoder |
| Frontend | HTML/CSS/JS (Jinja2 templates) |

---

## Project Structure

```
BankBot-Pw-Skills/
├── app.py                        # Flask application entry point
├── model/
│   ├── random_forest_model.pkl   # Trained Random Forest classifier
│   ├── tfidf_vectorizer.pkl      # Fitted TF-IDF vectorizer
│   └── label_encoder.pkl         # Fitted label encoder
├── templates/
│   └── index.html                # Chat UI
├── static/                       # CSS / JS assets
├── requirements.txt              # Python dependencies
├── app.log                       # Runtime log file
├── Architecutre Document.pdf
├── Detailed Project Report.pdf
├── HLD Document.pdf
├── LLD Document.pdf
└── Wireframe Document.pdf
```

---

## How It Works

1. User types a banking question in the web UI.
2. `app.py` receives the POST request at `/ask`.
3. The question is preprocessed:
   - Lowercased
   - Digits removed
   - Punctuation removed
4. Preprocessed text is vectorized with the loaded TF-IDF vectorizer.
5. The Random Forest model predicts the answer class label.
6. The label encoder decodes the prediction back to a human-readable answer.
7. The answer is returned as JSON `{"answer": "..."}`.

---

## Setup & Running

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
git clone https://github.com/jaideepj2004/BankBot-Pw-Skills.git
cd BankBot-Pw-Skills
pip install -r requirements.txt
```

### Run

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

---

## API Reference

### `GET /`
Returns the chat interface (HTML).

### `POST /ask`
Accepts a JSON body and returns a predicted banking answer.

**Request:**
```json
{
  "question": "How do I open a savings account?"
}
```

**Response:**
```json
{
  "answer": "You can open a savings account by visiting your nearest branch or through the mobile app."
}
```

---

## Documentation

Full project documentation is included in the repository:

| Document | Description |
|---|---|
| `Architecutre Document.pdf` | System architecture overview |
| `HLD Document.pdf` | High-Level Design |
| `LLD Document.pdf` | Low-Level Design |
| `Wireframe Document.pdf` | UI wireframes |
| `Detailed Project Report.pdf` | Complete project report |
