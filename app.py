from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, template_folder='Templates')

OWNER_CODE = "drith2015"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/unlock")
def unlock():
    return render_template("unlock.html")

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
