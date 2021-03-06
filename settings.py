import os
from configparser import ConfigParser

config = ConfigParser()

config_filename = "config.ini"


def write_config():
    config.write(open(config_filename, 'w'))


def initialize_config():
    if not os.path.exists(config_filename):
        write_config()
    config.read(config_filename)


def check_section(section):
    if not config.has_section(section):
        config.add_section(section)
        write_config()


def add_setting(section, setting, value):
    check_section(section)
    config.set(section, setting, value)
    write_config()


def get_value(section, setting):
    return config.get(section, setting)
