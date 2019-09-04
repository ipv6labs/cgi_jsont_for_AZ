import time
import os
import platform

from datetime import datetime
from socket import gethostname


from flask import Flask
app = Flask(__name__)

@app.route("/")

print(' "id": "'+platform.node()+'",')
