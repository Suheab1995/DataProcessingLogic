# data_generation_service/app.py
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/generate')
def generate_data():
    data = [random.randint(1, 100) for _ in range(10)]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
