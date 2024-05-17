# user_service.py (Microservice to display users)

from flask import Flask, jsonify

app = Flask(__name__)

# Dummy user data for demonstration
users = [
    {'username': 'user1'},
    {'username': 'user2'},
    {'username': 'user3'}
]

@app.route("/users")
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
