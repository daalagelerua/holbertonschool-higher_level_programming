#!/usr/bin/python3

from flask import Flask, request, jsonify


users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

app = Flask(__name__)


@app.route('/')
def home():
    return ("Welcome to the Flask API!")


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route("/add_user", methods=['POST'])
def add_user():
    new_user = request.get_json()
    if 'username' not in new_user:
        return jsonify({"error": "Username is required"}), 400
    username = new_user['username']
    users[username] = {
        "username": new_user.get('username'),
        "name": new_user.get('name'),
        "age": new_user.get('age'),
        "city": new_user.get('city')
    }
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


@app.route('/users/<username>')
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


if __name__ == "__main__":
    app.run()
