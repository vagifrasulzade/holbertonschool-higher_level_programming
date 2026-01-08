#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Hello, this is a simple Flask API!"


@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    return "OK", 200


@app.route("/user/<username>", methods=["GET", "POST"])
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/user/<username>", methods=["POST"])
def create_user(username):
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    user_data = request.get_json()
    users[username] = user_data
    return jsonify({"message": "User created"}), 201


if __name__ == "__main__":
    app.run()
