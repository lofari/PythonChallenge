from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import Home, CargarInfraccion

# from .views import GetTokenPairView

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("cargar_infraccion/", CargarInfraccion.as_view(), name="cargar_infraccion"),
]