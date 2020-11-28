import os
from flask import Flask, jsonify

# Initialize the Flask app instance
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT"))