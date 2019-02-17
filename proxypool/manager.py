import sys
import os
from proxypool.db import RedisClient

class Manager(object):
    def __init__(self):
        self.redis = RedisClient()

    def init(self):
        self.redis.clear()
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def checkRedis(self):
        self.redis.check()