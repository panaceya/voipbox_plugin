from rest_framework.routers import APIRootView

from netbox.api.viewsets import NetBoxModelViewSet
from . import serializers
from .. import filters
from ..models import VoiceCircuit, Pool


class voipboxPluginRootView(APIRootView):
    """
    voipbox_plugin API root view
    """
    def get_view_name(self):
        return 'voipbox'

class PoolViewSet(NetBoxModelViewSet):
    queryset = Pool.objects.prefetch_related('tenant', 'region', 'tags')
    serializer_class = serializers.PoolSerializer
    filterset_class = filters.PoolFilterSet

class VoiceCircuitsViewSet(NetBoxModelViewSet):
    queryset = VoiceCircuit.objects.prefetch_related('tenant', 'region', 'tags')
    serializer_class = serializers.VoiceCircuitSerializer
    filterset_class = filters.VoiceCircuitFilterSet
