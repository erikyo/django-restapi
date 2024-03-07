from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ExampleAuthenticatedView(APIView):
    def get(self, request):
        return Response({"message": "Authenticated successfully!"})


@permission_classes([IsAdminUser])
class ExampleAdminOnlyView(APIView):
    def get(self, request):
        return Response({"message": "Welcome, admin user!"})


