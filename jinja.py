import os

def fileExists(name):
    return os.path.isfile(os.path.dirname(os.path.abspath(__file__)) + '/' + name)