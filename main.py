from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def execute():
    code = request.json.get("code", "")
    exec(code)
    return jsonify({"status": "executado"})

@app.route("/health", methods=["GET"])
def execute():
    return jsonify({ "status": "running" })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
