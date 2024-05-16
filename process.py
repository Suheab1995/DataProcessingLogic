# data_processing_service/app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    result = sum(data)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
