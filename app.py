from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello from Dr. ViKi DevOps Pipeline!<br><small>{datetime.utcnow().isoformat()}Z</small>"

@app.route("/health")
def health():
    return jsonify(status="ok", time=datetime.utcnow().isoformat())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8088)
