from flask import Flask
app = Flask(__name__)

TEST = HOGE

@app.route("/")

def hello():
    return "Hello World!!"
    return print(TEST)
