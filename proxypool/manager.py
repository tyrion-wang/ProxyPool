import sys
from proxypool.db import RedisClient
import os


class Manager(object):
    def __init__(self):
        self.redis = RedisClient()

    def init(self):
        self.redis.clear()
        python = sys.executable
        os.execl(python, python, *sys.argv)
