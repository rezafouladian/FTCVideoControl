import PyATEMMax

import settings

settings.load_config()

if not settings.check_section('atem'):
    settings.add_section('atem')
    # Initilize values
    settings.set_value('atem', 'enable_atem', 'false')
    settings.set_value('atem', 'number_of_atems', '0')
    settings.set_value('atem', 'atem1_hostname', "none")
    settings.set_value('atem', 'atem2_hostname', "none")
    settings.set_value('atem', 'atem3_hostname', "none")
    settings.set_value('atem', 'atem4_hostname', "none")
    settings.set_value('atem', 'atem1_type', "none")
    settings.set_value('atem', 'atem2_type', "none")
    settings.set_value('atem', 'atem3_type', "none")
    settings.set_value('atem', 'atem4_type', "none")


def reload_config():
    settings.load_config()
