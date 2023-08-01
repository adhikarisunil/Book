# books/views.py

from rest_framework import viewsets
from .models import Book, Nobel, Poem
from .serializers import BookSerializer, NobelSerializer, PoemSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class  NobelViewSet(viewsets.ModelViewSet):
    queryset = Nobel.objects.all()
    serializer_class = NobelSerializer

class  PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    pass