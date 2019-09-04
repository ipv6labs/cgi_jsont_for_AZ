from flask import Flask
app = Flask(__name__)

import time
import os
import platform

from datetime import datetime
from socket import gethostname


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/jsont")
def jsont():
    #return "jsont run"
    print(' "pf": "'+platform.system()+' '+platform.machine()+'",')
