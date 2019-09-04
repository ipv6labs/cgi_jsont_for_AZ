import time
import os
import platform

from datetime import datetime
from socket import gethostname

from flask import Flask, jsonify
app = Flask(__name__)

print_leep = '36'
print_next = '1483228800'
print_step = '1'

@app.route("/")
def hello():
    return "README https://www.example.jp/"

@app.route("/cgi-bin/time")
def exec_time():
    return datetime.now()

@app.route("/cgi-bin/jst")
def exec_jst():
    return "{0:.3f}".format(time.time())

@app.route("/cgi-bin/ntp")
def exec_ntp():
    return "{0:.3f}".format(time.time() + 2208988800)

@app.route("/cgi-bin/json")
def exec_json():
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
    return result
