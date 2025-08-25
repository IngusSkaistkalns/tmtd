from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "<h1>Welcome to TMTD!</h1>"