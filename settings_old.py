import os
from configparser import ConfigParser

config = ConfigParser()

config_filename = "config.ini"


def write_config():
    config.write(open(config_filename, 'w'))


def load_config():
    if not os.path.exists(config_filename):
        write_config()
    config.read(config_filename)


def check_section(section):
    if config.has_section(section):
        return True
    else:
        return False


def add_section(section):
    if not config.has_section(section):
        config.add_section(section)


def get_value(section, option):
    return config.get(section, option)


def set_value(section, option, value):
    if not config.has_section(section):
        config.add_section(section)
    config.set(section, option, value)
