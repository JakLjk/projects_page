from config import ENV_USE_DEV_SETTINGS

if ENV_USE_DEV_SETTINGS:
    from .dev_settings import *
if not ENV_USE_DEV_SETTINGS:
    from .prod_settings import *