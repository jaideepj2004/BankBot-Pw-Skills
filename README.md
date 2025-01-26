# BankBot Project -- NLP internship at Physics Wallah

## Project Description

**Name:** BankBot  
**Purpose:** A chatbot to answer banking-related queries.  
**Internship:** Developed for a remote internship at Physics Wallah.  
**Deployment:** Hosted on Render with an integrated CI/CD pipeline for seamless updates.

## Features

### Natural Language Processing (NLP)
- Processes user queries using a pre-trained Random Forest model.
- Converts text into meaningful features using TF-IDF Vectorization.

### Banking Queries
- Handles FAQs related to banking, such as account information, interest rates, and other common queries.

### Python Logging
- Logs events and errors for better monitoring and debugging.

### Flask Web App
- Provides a web interface for user interaction.

### Frontend
- Built using HTML, CSS, and JavaScript for a smooth user experience.

### Deployment
- Render hosting ensures high availability.
- CI/CD pipeline automates testing and deployment.

## Technologies Used

- **Programming Language:** Python
- **Libraries:**  
  - Flask (Web framework)  
  - scikit-learn (Machine learning)  
  - pandas, numpy (Data processing)  
  - nltk (Text preprocessing)  
  - pickle (Model storage)
- **Frontend:**  
  - HTML, CSS, and JavaScript for the user interface.
- **Tools:**  
  - Virtual Environment for isolated development.  
  - Render for deployment.  
  - CI/CD pipeline for streamlined updates.

## Setup Instructions

1. **Clone the Repository:**
    ```bash
    git clone <repo-link>
    cd BankBot
    ```

2. **Activate Virtual Environment:**
    ```bash
    python -m venv myenv
    myenv\Scripts\activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Locally:**
    ```bash
    python app.py
    ```

5. **Access Locally:**  
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in a browser.

6. **Render Deployment:**  
   Follow the repository's pipeline configuration for automatic deployment and updates.

## Usage

- Interact through the web interface or via the API (`/ask` endpoint).
- End the chat by using a specific command (e.g., "aaa").

## Key Files

- **app.py:** Flask application logic.
- **model/random_forest_model.pkl:** Pre-trained Random Forest model.
- **model/tfidf_vectorizer.pkl:** TF-IDF vectorizer for text features.
- **model/label_encoder.pkl:** Encoder for mapping predictions to answers.
- **requirements.txt:** List of dependencies.
- **render.yaml or equivalent:** Configuration for Render deployment and CI/CD pipeline.
- **templates/index.html:** Frontend HTML structure.
- **static/css/styles.css:** Stylesheet for the frontend.
- **static/js/scripts.js:** JavaScript for interactive elements on the frontend.

## Acknowledgment

Special thanks to **Physics Wallah** for this internship opportunity.
