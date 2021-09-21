from configparser import ConfigParser
import os

config = ConfigParser()

if not os.path.exists('config.ini'):
    config.write(open('config.ini', 'w'))