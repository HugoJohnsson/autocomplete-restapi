import os
import sys
from flask import Flask, jsonify 
from service.prefix_tree_service import prefix_tree_service

# Initialize the Flask app instance
app = Flask(__name__)

# Load all words in the database into the prefix tree
words_file = open("words.txt", "r")
lines = words_file.readlines()

for line in lines:
    word = line.strip()
    
    if len(word) > 2:
        prefix_tree_service.insert(word)


@app.route("/api/v1/match/<prefix>")
def match(prefix):
    matches = prefix_tree_service.get_matching_phrases(prefix)

    return jsonify(matches)

@app.route("/api/v1/insert/<phrase>")
def insert(phrase):
    res = {"success": False}

    try:
        prefix_tree_service.insert(phrase)
        res["success"] = True
    except:
        pass

    return jsonify(res)    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT"))