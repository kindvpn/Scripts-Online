from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/server/online")
def online_users():
    result = subprocess.getoutput("ss -ntp | grep ESTAB | wc -l")
    return jsonify({"online_users": int(result)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
