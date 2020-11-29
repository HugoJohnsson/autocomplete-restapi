import os
from flask import Flask, jsonify
from prefix_tree.prefix_tree import PrefixTree

tree = PrefixTree()

tree.insert_prefix("hugo")
tree.insert_prefix("hej")
tree.insert_prefix("hejsan")

tree.print_tree(tree.root)

#print(tree.hasWord("hugo"))
#print(tree.hasWord("hejsan"))
#print(tree.hasWord("heja"))

# Initialize the Flask app instance
app = Flask(__name__)

@app.route("/api/v1")
def hello():
    return jsonify({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("PORT"))