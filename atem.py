import settings

settings.load_config()

if not settings.check_section('atem'):
    settings.add_section('atem')
    settings.set_value('atem', 'enable_atem', 'false')
