from config import ENV_USE_DEV_SETTINGS

if ENV_USE_DEV_SETTINGS:
    print("Using dev settings")
    from .dev_settings import *
if not ENV_USE_DEV_SETTINGS:
    print("Using prod settings")
    from .prod_settings import *