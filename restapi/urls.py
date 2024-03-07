# urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_v1 import views

# Import drf-yasg modules
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# New router for product and categories under the "v1" prefix
v1_router = routers.DefaultRouter()
v1_router.register(r'products', views.ProductViewSet)
v1_router.register(r'categories', views.CategoryViewSet)

# Swagger documentation setup
schema_view = get_schema_view(
    openapi.Info(
        title="Your API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include the "v1" prefix for product and categories
    path('api/v1/', include(v1_router.urls)),

    # Include the default authentication endpoints
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Swagger documentation URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]