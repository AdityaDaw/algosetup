import os
from configparser import ConfigParser


class CustomConfigParser(ConfigParser):
    def __init__(self, filepath):
        super().__init__()
        self.read(filepath)

    def getVariable(self, keyname: str):
        return self.get('DEFAULT', keyname)


def readContext() -> CustomConfigParser:
    configfile = os.path.dirname(os.path.realpath(__file__) )+ "/config.ini"
    config = CustomConfigParser(configfile)
    return config