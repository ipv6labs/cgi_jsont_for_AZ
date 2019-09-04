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
    result = jsont( {
      "pf": _my_pf_sys,
    "hoge": 1
    } )
    return jsonify(result)
