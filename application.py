import time
import os
import platform

from datetime import datetime
from socket import gethostname
from datetime import datetime, timedelta, timezone

from flask import Flask, jsonify
app = Flask(__name__)

print_leep = '36'
print_next = '1483228800'
print_step = '1'

@app.route("/")
def hello():
    return "README https://www.example.jp/"

@app.route("/ntp")
def _exec_ntp():
    return "EXEC ntp!"

@app.route("/cgi-bin/time")
def exec_time():
    JST = timezone(timedelta(hours=+9), 'JST')
    return datetime.now(JST)

@app.route("/cgi-bin/jst")
def exec_jst():
    return "{0:.3f}".format(time.time())

@app.route("/jsont")
def jsont():
    result = {
      "id": platform.node(),
      "os": platform.system(),
    "arch": platform.machine(),
      "it": 0.000,
      "st": "{0:.3f}".format(time.time()),
    "leep": print_leep,
    "next": print_next,
    "step": print_step
    }
    return jsonify(result)
