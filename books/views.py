# books/views.py

from rest_framework import viewsets
from .models import Book, Nobel, Poem
from .serializers import BookSerializer, NobelSerializer, PoemSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']

class  NobelViewSet(viewsets.ModelViewSet):
    queryset = Nobel.objects.all()
    serializer_class = NobelSerializer   
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']  

class  PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']

class CustomTokenObtainPairView(TokenObtainPairView):
    pass