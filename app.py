from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir conexiones desde el frontend

DEBUG_MODE = os.getenv("DEBUG_MODE", "False") == "True"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    if 'love' in text or 'great' in text:
        sentiment = 'positive'
    elif 'hate' in text or 'bad' in text:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=DEBUG_MODE)
