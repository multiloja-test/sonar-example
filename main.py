from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def execute():
    code = request.json.get("code", "")
    exec(code)
    return jsonify({"status": "executado"})

@app.route("/health", methods=["GET"])
def execute():
    return jsonify({ "status": "running" })

@app.route("/users/search", methods=["GET"])
def search_users():
    username = request.args.get("username", "")

    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE users (username TEXT)"
    )
    connection.execute(
        "INSERT INTO users VALUES ('alice')"
    )

    query = f"SELECT username FROM users WHERE username = '{username}'"
    results = connection.execute(query).fetchall()
    connection.close()

    return jsonify({"users": results})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
