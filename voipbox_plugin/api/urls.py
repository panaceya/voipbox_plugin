from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.APIRootView = views.voipboxPluginRootView

router.register(r'pool', views.PoolViewSet)
router.register(r'voice-circuits', views.VoiceCircuitsViewSet)

app_name = "voipbox_plugin-api"
urlpatterns = router.urls
