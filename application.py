import time
import os
import platform

from datetime import datetime
from socket import gethostname

from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/jsont")
def jsont():
    _my_pf_sys = platform.system()
    result = {
      "it": 0,
      "pf": platform.system() platform.machine(),
    "hoge": 1
    }
    return jsonify(result)
