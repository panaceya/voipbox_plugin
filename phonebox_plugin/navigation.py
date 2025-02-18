from packaging import version
from django.conf import settings

from netbox.plugins import PluginMenuItem, PluginMenu

plugin_settings = settings.PLUGINS_CONFIG["phonebox_plugin"]


plugin_menu = (
    PluginMenuItem(
        link='plugins:phonebox_plugin:list_view',
        link_text='Numbers',
        buttons=()
    ),
    PluginMenuItem(
        link='plugins:phonebox_plugin:voice_circuit_list_view',
        link_text='Voice Circuits',
        buttons=()
    ),
)

if plugin_settings.get("top_level_menu"):
    menu = PluginMenu(
        label="PhoneBox Plugin",
        groups=(("", plugin_menu),),
        icon_class="mdi mdi-phone-dial",
    )
else:
    menu_items = plugin_menu
