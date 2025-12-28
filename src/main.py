from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Congratulations!<br>Your application is running in Azure Cloud</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

