from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Cloud CI/CD Lab - Version 2"

@app.route("/student")
def student():
    return {
        "name": "Student",
        "course": "Cloud Computing and DevOps",
        "version": "1.0"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
