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
    return "Hello World!"

@app.route("/jsont")
def jsont():
    _my_pf_sys = print(platform.system()+' '+platform.machine())
    result = {
      "it": 0.000,
      "pf": _my_pf_sys,
      "st": "{0:.3f}".format(time.time()),
    "leep": print_leep,
    "next": print_next,
    "step": print_step
    }
    return jsonify(result)
