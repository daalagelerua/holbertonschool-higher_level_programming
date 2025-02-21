#!/usr/bin/python3

from flask import Flask, request, jsonify
from markupsafe import escape


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
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    new_user = {
        data.get('username'): {
            key: value for key, value in data.items() if key != "username"}}
    users.update(new_user)
    return jsonify(new_user), 201


@app.route('/users/<username>')
def get_user(username):
    user_data = users.get(escape(username))
    if user_data:
        return jsonify({"username": username, **user_data})
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run()
