from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_ world():
    return "Hello WorldS!"
