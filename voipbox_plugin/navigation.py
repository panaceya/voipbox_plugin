from packaging import version
from django.conf import settings

from netbox.plugins import PluginMenuItem, PluginMenu, PluginMenuButton

plugin_settings = settings.PLUGINS_CONFIG["voipbox_plugin"]


plugin_menu = (
    PluginMenuItem(
        link='plugins:voipbox_plugin:pool_list',
        link_text='Pools',
        permissions=["voipbox_plugin.view_pool"],
        buttons=(
            PluginMenuButton(
                link="plugins:voipbox_plugin:pool_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                permissions=["voipbox_plugin.add_pool"],
            ),
            PluginMenuButton(
                link="plugins:voipbox_plugin:pool_bulk_import",
                title="Import",
                icon_class="mdi mdi-upload",
                permissions=["voipbox_plugin.add_pool"],
            ),
        ),
    ),
    PluginMenuItem(
        link='plugins:voipbox_plugin:voicecircuit_list',
        link_text='Voice Circuits',
        permissions=["voipbox_plugin.view_voicecircuit"],
        buttons=(
            PluginMenuButton(
                link="plugins:voipbox_plugin:voicecircuit_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                permissions=["voipbox_plugin.add_voicecircuit"],
            ),
            PluginMenuButton(
                link="plugins:voipbox_plugin:voicecircuit_bulk_import",
                title="Import",
                icon_class="mdi mdi-upload",
                permissions=["voipbox_plugin.add_voicecircuit"],
            ),
        ),
    ),
)

if plugin_settings.get("top_level_menu", True):
    menu = PluginMenu(
        label="voipbox Plugin",
        groups=(("Voice", plugin_menu),),
        icon_class="mdi mdi-phone-dial",
    )
else:
    menu_items = plugin_menu
