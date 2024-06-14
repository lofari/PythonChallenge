
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.views import GenerarInforme

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls")),
    path("generar_informe/", GenerarInforme.as_view(), name='generar_informe'),
    path("get/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/schema/", SpectacularAPIView.as_view(), name='schema'),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    # path("get/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]
