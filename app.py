from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API Running"

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    return jsonify({"result": a + b})

@app.route("/multiply", methods=["GET"])
def multiply():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return jsonify({"result": a * b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)