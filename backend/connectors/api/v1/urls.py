from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136388ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136388", Testconnectors136388ViewSet, basename="testconnectors136388"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
