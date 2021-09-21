import settings

settings.load_config()

if not settings.check_section('tricaster'):
    settings.add_section('tricaster')
    # Initilize values
    settings.set_value('tricaster', 'enable_tricaster', 'false')
