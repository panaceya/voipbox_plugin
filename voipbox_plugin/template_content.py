from netbox.plugins import PluginTemplateExtension

from .models import Pool

__all__ = (
    "template_extensions",
)

class DevicePoolLink(PluginTemplateExtension):
    models = ["dcim.device"]

    def right_page(self):
        device = self.context["object"]
        pools = Pool.objects.filter(device=device).select_related(
            "provider", "forward_to"
        )

        if not pools.exists():
            return ""

        return self.render(
            "voipbox_plugin/device_pool_links.html",
            extra_context={"pools": pools},
        )


template_extensions = (
    DevicePoolLink,
)
