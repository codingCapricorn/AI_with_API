# -*- coding: utf-8 -*-
"""Q2_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zlHWoKc6c1YhhaYgWMtv8qogB2tomsT-
"""

pip install Flask openai

from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

def check_loan_eligibility(customer_data):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Based on the following customer data, determine loan eligibility (Approved/Rejected) and provide a recommendation: {customer_data}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

@app.route('/loan-eligibility', methods=['POST'])
def loan_eligibility():
    data = request.json
    customer_data = data.get('customer_data')
    eligibility = check_loan_eligibility(customer_data)
    return jsonify({"eligibility": eligibility})

if __name__ == '__main__':
    app.run(debug=True)