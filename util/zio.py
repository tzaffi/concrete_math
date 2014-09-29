__author__ = 'zephaniahgrunschlag'

import sys


class RedirectStdout:
    def __init__(self, target):
         self.stdout = sys.stdout
         self.target = target

    def __enter__(self):
        sys.stdout = self.target

    def __exit__(self, type, value, tb):
        sys.stdout = self.stdout
