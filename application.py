import time
import os
import platform

from datetime import datetime
from socket import gethostname

from flask import Flask, jsonify
app = Flask(__name__)

# Sep 05 2019
print_leep = '36'
print_next = '1483228800'
print_step = '1'


@app.route("/")
def hello():
    return "OK"


@app.route("/platform")
def hello():
    return platform.platform()


@app.route("/cgi-bin/time")
def exec_time():
    result_time = time.strftime('%a %b %d %X %Y %Z')
    return result_time


@app.route("/cgi-bin/jst")
def exec_jst():
    result_jst = "{0:.3f}".format(time.time())
    return result_jst


@app.route("/cgi-bin/ntp")
def exec_ntp():
    result_ntp = "{0:.3f}".format(time.time() + 2208988800)
    return result_ntp


@app.route("/cgi-bin/json")
def exec_json():
    result_json = {
      "id": platform.node(),
      "os": platform.system(),
    "arch": platform.machine(),
      "it": "{0:.3f}".format(0.000),
      "st": "{0:.3f}".format(time.time()),
    "leep": print_leep,
    "next": print_next,
    "step": print_step
    }
    return jsonify(result_json)


@app.route("/cgi-bin/jsont")
def jsont():
    result_jsont = "No Support"
    return result_jsont
