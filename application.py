#!/opt/python/3/bin/python

import time
import os
import platform

from datetime import datetime
from socket import gethostname

print_leep = '36'
print_next = '1483228800'
print_step = '1'

# HTTP Header
print('Access-Control-Allow-Origin: *')
print('Cache-Control: no-cache, no-store')
print('Content-type: application/javascript'"\n")

# HTTP Body
print('jsont( {')
print(' "id": "'+platform.node()+'",')
print(' "pf": "'+platform.system()+' '+platform.machine()+'",')
print(' "it": 0.000,')
print(' "st": '+"{0:.3f}".format(time.time())+',')
print(' "leep": '+print_leep+',')
print(' "next": '+print_next+',')
print(' "step": '+print_step)
print('} )')
