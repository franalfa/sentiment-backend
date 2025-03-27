# Sentiment Backend (Ready for Render)

This is a simple Flask-based backend for sentiment analysis. Designed to be deployed on Render.com with HTTPS.

## Endpoint

- **POST** `/analyze`
- **Body:** `{ "text": "I love this app!" }`
- **Response:** `{ "sentiment": "positive" }`

## Running locally
```
pip install -r requirements.txt
python app.py
```
