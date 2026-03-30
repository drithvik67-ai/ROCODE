from flask import Flask, send_from_directory, request, jsonify
import os

app = Flask(__name__)

# Get the directory where app.py lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OWNER_CODE = "drith2015"

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/unlock")
def unlock():
    return send_from_directory(BASE_DIR, "unlock.html")

@app.route("/verify-owner", methods=["POST"])
def verify_owner():
    data = request.get_json()
    code = data.get("code", "")
    if code == OWNER_CODE:
        return jsonify({"success": True, "message": "Owner access granted!"})
    return jsonify({"success": False, "message": "Invalid code"}), 403

@app.route("/health")
def health():
    return jsonify({"status": "ok", "site": "RoCodesX"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
