# -*- coding: utf-8 -*-
"""Q4_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zlHWoKc6c1YhhaYgWMtv8qogB2tomsT-
"""

pip install Flask openai

!pip install fastapi uvicorn

from flask import Flask, request, jsonify
import time

app = Flask(__name__)

rate_limit = {}

def is_rate_limited(user_id):
    current_time = time.time()
    if user_id not in rate_limit:
        rate_limit[user_id] = {"tokens": 5, "last_time": current_time}
        return False

    time_passed = current_time - rate_limit[user_id]["last_time"]
    rate_limit[user_id]["tokens"] += time_passed * 1  # 1 token per second
    rate_limit[user_id]["last_time"] = current_time

    if rate_limit[user_id]["tokens"] > 5:
        rate_limit[user_id]["tokens"] = 5

    if rate_limit[user_id]["tokens"] >= 1:
        rate_limit[user_id]["tokens"] -= 1
        return False
    else:
        return True

# Add a root route to avoid blank screen
@app.route('/')
def home():
    return "Welcome to the Banking API! Use the /transaction endpoint to process transactions."

@app.route('/transaction', methods=['POST'])
def transaction():
    user_id = request.headers.get('User-ID')
    if not user_id:
        return jsonify({"error": "User-ID header missing"}), 400

    if is_rate_limited(user_id):
        return jsonify({"error": "Rate limit exceeded"}), 429

    # Process transaction
    return jsonify({"message": "Transaction processed"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)