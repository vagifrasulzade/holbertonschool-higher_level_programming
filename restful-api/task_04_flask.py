#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    return "Hello, this is a simple API!", 200


@app.route("/status", methods=["GET"])
def status():
    return "OK", 200


@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users.keys())), 200


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json(silent=True) or {}

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = data
    return jsonify({"message": "User added"}), 201


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username]), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)
