
from flask import Flask, request, jsonify
import update_data
import subprocess
import os

app = Flask(__name__)

API_TOKEN = os.environ.get("API_TOKEN", "YOUR_SECRET_TOKEN")

@app.route("/")
def home():
    return "✅ Render API is running."

@app.route("/update", methods=["POST"])
def update():
    token = request.args.get("token")
    if token != API_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401

    success = update_data.run()
    if success:
        try:
            subprocess.run(["git", "add", "frontend-cloudflare/data/growth.csv"], check=True)
            subprocess.run(["git", "commit", "-m", "update growth.csv"], check=True)
            subprocess.run(["git", "push"], check=True)
            return jsonify({"message": "✅ 成功更新並 push 到 GitHub"})
        except Exception as e:
            return jsonify({"error": f"Git push failed: {e}"}), 500
    return jsonify({"error": "資料更新失敗"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
