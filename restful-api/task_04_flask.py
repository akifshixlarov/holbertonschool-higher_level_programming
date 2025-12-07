#!/usr/bin/python3
"""A first Flask API"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    """Return welcome message"""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_json_data():
    """Return list of usernames"""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return API status"""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def user_profile(username):
    """Return user data"""
    profile = users.get(username)
    if not profile:
        return jsonify({"error": "User not found"}), 404
    return jsonify(profile)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user"""
    user_data = request.get_json()

    # Invalid JSON
    if not user_data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = user_data.get("username")

    # Username missing
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Duplicate username
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Create user object
    profile = {
        "username": username,
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }

    users[username] = profile

    return jsonify({"message": "User added", "user": profile}), 201


if __name__ == "__main__":
    app.run(debug=True)
