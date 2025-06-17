from django.utils.translation import gettext_lazy as _
from netbox.views import generic
from utilities.views import ViewTab, register_model_view

from . import filters
from . import forms
from . import tables
from .models import VoiceCircuit, Pool


@register_model_view(Pool, "list", path="", detail=False)
class PoolListView(generic.ObjectListView):
    queryset = Pool.objects.all()
    filterset = filters.PoolFilterSet
    filterset_form = forms.PoolFilterForm
    table = tables.PoolTable
    template_name = 'voipbox_plugin/pool_list.html'


@register_model_view(Pool)
class PoolView(generic.ObjectView):
    queryset = Pool.objects.prefetch_related('parent')
    child_model = Pool
    template_name = "voipbox_plugin/pool.html"
    tab = ViewTab(
        label=_('Child pools'),
        badge=lambda x: x.get_children().count(),
        permission='plugins:voipbox_plugin:view_pool',
        weight=600
    )


@register_model_view(Pool, "add", detail=False)
@register_model_view(Pool, "edit")
class PoolEditView(generic.ObjectEditView):
    queryset = Pool.objects.all()
    form = forms.PoolEditForm


@register_model_view(Pool, "bulk_edit", path="edit", detail=False)
class PoolBulkEditView(generic.BulkEditView):
    queryset = Pool.objects.prefetch_related('parent')
    filterset = filters.PoolFilterSet
    table = tables.PoolTable
    form = forms.PoolBulkEditForm


@register_model_view(Pool, "delete")
class PoolDeleteView(generic.ObjectDeleteView):
    queryset = Pool.objects.all()


@register_model_view(Pool, "bulk_delete", path="delete", detail=False)
class PoolBulkDeleteView(generic.BulkDeleteView):
    queryset = Pool.objects.filter()
    filterset = filters.PoolFilterSet
    table = tables.PoolTable


@register_model_view(Pool, "bulk_import", detail=False)
class PoolBulkImportView(generic.BulkImportView):
    queryset = Pool.objects.all()
    model_form = forms.PoolCSVForm
    table = tables.PoolTable


@register_model_view(VoiceCircuit, "list", path="", detail=False)
class VoiceCircuitListView(generic.ObjectListView):
    queryset = VoiceCircuit.objects.all()
    filterset = filters.VoiceCircuitFilterSet
    filterset_form = forms.VoiceCircuitFilterForm
    table = tables.VoiceCircuitTable


@register_model_view(VoiceCircuit)
class VoiceCircuitView(generic.ObjectView):
    queryset = VoiceCircuit.objects.prefetch_related('tenant')
    template_name = "voipbox_plugin/voicecircuit.html"


@register_model_view(VoiceCircuit, "add", detail=False)
@register_model_view(VoiceCircuit, "edit")
class VoiceCircuitEditView(generic.ObjectEditView):
    queryset = VoiceCircuit.objects.all()
    form = forms.VoiceCircuitEditForm


@register_model_view(VoiceCircuit, "bulk_edit", path="edit", detail=False)
class VoiceCircuitBulkEditView(generic.BulkEditView):
    queryset = VoiceCircuit.objects.prefetch_related('tenant')
    filterset = filters.VoiceCircuitFilterSet
    table = tables.VoiceCircuitTable
    form = forms.VoiceCircuitBulkEditForm


@register_model_view(VoiceCircuit, "delete")
class VoiceCircuitDeleteView(generic.ObjectDeleteView):
    queryset = VoiceCircuit.objects.all()


@register_model_view(VoiceCircuit, "bulk_delete", path="delete", detail=False)
class VoiceCircuitBulkDeleteView(generic.BulkDeleteView):
    queryset = VoiceCircuit.objects.filter()
    filterset = filters.VoiceCircuitFilterSet
    table = tables.VoiceCircuitTable


@register_model_view(VoiceCircuit, "bulk_import", detail=False)
class VoiceCircuitBulkImportView(generic.BulkImportView):
    queryset = VoiceCircuit.objects.all()
    model_form = forms.VoiceCircuitCSVForm
    table = tables.VoiceCircuitTable
