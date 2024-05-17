# app.py (Flask application)

from flask import Flask, jsonify, render_template, request, redirect, url_for
import socket

app = Flask(__name__)

# Dummy user data for demonstration
users = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'},
    {'username': 'user3', 'password': 'password3'}
]

# Function to fetch hostname and ip
def fetchDetails():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname), str(host_ip)

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for user in users:
            if user['username'] == username and user['password'] == password:
                return redirect(url_for('dashboard'))
        return render_template('login.html', message='Invalid username or password')
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', users=users)

@app.route("/details")
def details():
    hostname, ip = fetchDetails()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
