#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:tyrion
@file: testAPI.py
@time: 2019/02/{DAY}
"""

from proxypool.api2 import app
from proxypool.setting import *

#app.run('0.0.0.0', '5555')
app.run(host='0.0.0.0' ,port=8888)