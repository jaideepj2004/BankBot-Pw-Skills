import logging
from flask import Flask, request, jsonify, render_template
import pickle
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set logging level to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file named app.log
        logging.StreamHandler()  # Log to console as well
    ]
)

logging.info("Starting Flask application.")

# Load the pre-trained models, vectorizer, and label encoder
try:
    with open('model/random_forest_model.pkl', 'rb') as file:
        best_rf_model = pickle.load(file)
    logging.info("Random Forest model loaded successfully.")

    with open('model/tfidf_vectorizer.pkl', 'rb') as file:
        vectorizer = pickle.load(file)
    logging.info("TF-IDF vectorizer loaded successfully.")

    with open('model/label_encoder.pkl', 'rb') as file:
        encoder = pickle.load(file)
    logging.info("Label encoder loaded successfully.")

except Exception as e:
    logging.error(f"Error loading model files: {e}")
    raise

# Preprocessing function for user input
def preprocess_text(text):
    try:
        logging.debug(f"Preprocessing text: {text}")
        text = text.lower()  # Convert to lowercase
        text = re.sub(r'\d+', '', text)  # Remove digits
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        logging.debug(f"Cleaned text: {text}")
        return text
    except Exception as e:
        logging.error(f"Error during text preprocessing: {e}")
        raise

# Route to handle user input and predict the answer
@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_input = request.json['question']
        logging.info(f"Received user input: {user_input}")
        cleaned_input = preprocess_text(user_input)
        input_tfidf = vectorizer.transform([cleaned_input])

        predicted_class = best_rf_model.predict(input_tfidf)
        predicted_answer = encoder.inverse_transform(predicted_class)

        logging.info(f"Predicted answer: {predicted_answer[0]}")
        return jsonify({'answer': predicted_answer[0]})
    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

# Home route to render the HTML page
@app.route('/')
def home():
    logging.info("Rendering home page.")
    return render_template('index.html')

# Start the Flask app
if __name__ == '__main__':
    try:
        logging.info("Starting the Flask app.")
        app.run(debug=True)
    except Exception as e:
        logging.critical(f"Critical error occurred: {e}")
        raise
