import os
from flask import Flask, jsonify 
from service.prefix_tree_service import prefix_tree_service


# Initialize the Flask app instance
app = Flask(__name__)

@app.route("/api/v1/match/<prefix>")
def hello(prefix):
    matches = prefix_tree_service.get_matching_phrases(prefix)

    return jsonify({"result": matches})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT"))