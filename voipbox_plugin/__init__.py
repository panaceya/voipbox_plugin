import importlib.metadata
from netbox.plugins import PluginConfig

class VOIPBoxConfig(PluginConfig):
    name = 'voipbox_plugin'
    version = importlib.metadata.version('voipbox-plugin')
    verbose_name = 'VOIPBox Plugin'
    description = 'Telephone Number Management Plugin for NetBox.'
    author = 'Igor Korotchenkov'
    author_email = 'iDebugAll@gmail.com'
    base_url = 'voipbox'
    min_version = "4.3.0"
    max_version = "4.5.0"
    required_settings = []
    default_settings = {}
    caching_config = {
        '*': None
    }

config = VOIPBoxConfig
