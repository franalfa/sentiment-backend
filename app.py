from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
CORS(app)
auth = HTTPBasicAuth()

# Usuarios válidos
users = {
    "admin": generate_password_hash("secure123")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

DEBUG_MODE = os.getenv("DEBUG_MODE", "False") == "True"

@app.route('/analyze', methods=['POST'])
@auth.login_required
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
