from os.path import abspath, dirname

ROOT = dirname(dirname(abspath(__file__)))


def get_root():
    return ROOT
