import os
from flask import Flask, jsonify 
from service.prefix_tree_service import prefix_tree_service

import redis

r = redis.Redis(
host='redis',
port=6379,
password='')

r.set('foo', 'bar')
value = r.get('foo')
print(value)


# Initialize the Flask app instance
app = Flask(__name__)

@app.route("/api/v1/match/<prefix>")
def match(prefix):
    matches = prefix_tree_service.get_matching_phrases(prefix)

    return jsonify({"result": matches})

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