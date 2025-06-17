from django.urls import path, include
from . import views
from utilities.urls import get_model_urls

app_name = "voipbox_plugin"

urlpatterns = (
    path(
        "pool/",
        include(get_model_urls("voipbox_plugin", "pool", detail=False)),
    ),
    path(
        "pool/<int:pk>/",
        include(get_model_urls("voipbox_plugin", "pool")),
    ),
    path(
        "voicecircuits/",
        include(get_model_urls("voipbox_plugin", "voicecircuit", detail=False)),
    ),
    path(
        "voicecircuits/<int:pk>/",
        include(get_model_urls("voipbox_plugin", "voicecircuit")),
    ),
)
