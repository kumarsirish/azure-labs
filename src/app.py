from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Congratulations!<br>Your application is running in Azure Cloud</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

