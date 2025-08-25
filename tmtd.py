from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def recognize():
    # For now, return a placeholder response
    # Later this will use the model.h5 to predict the digit
    return jsonify({"prediction": "5"})
