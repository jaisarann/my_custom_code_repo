import os
import sys

import numpy
import requests

print(sys.version)
print(sys.executable)
print('hello world')
r = requests.get('http://www.google.com')
print('-' * 20)
print(r.status_code)

