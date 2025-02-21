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

    username = data.get('username')

    if username in users:
        return jsonify({"error": "User already exists"}), 409

    required_fields = {"name", "age", "city"}
    if not required_fields.issubset(data):
        return jsonify({"error":
                        "Missing required fields (name, age, city)"}), 400
    new_user = {
        username: {
            "name": data["name"],
            "age": data["age"],
            "city": data["city"]
        }
    }

    users.update(new_user)
    return jsonify({"message": "User added",
                    "user": new_user[username]}), 201


@app.route('/users/<username>')
def get_user(username):
    user_data = users.get(escape(username))
    if user_data:
        return jsonify({"username": username, **user_data})
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run()
