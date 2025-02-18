from packaging import version
from django.conf import settings

from netbox.plugins import PluginConfig

class PhoneBoxConfig(PluginConfig):
    name = 'phonebox_plugin'
    verbose_name = 'PhoneBox Plugin'
    description = 'Telephone Number Management Plugin for NetBox.'
    version = 'v0.0.11'
    author = 'Igor Korotchenkov'
    author_email = 'iDebugAll@gmail.com'
    base_url = 'phonebox'
    min_version = "4.2.0"
    max_version = "4.2.99"
    required_settings = []
    default_settings = {}
    caching_config = {
        '*': None
    }

config = PhoneBoxConfig
