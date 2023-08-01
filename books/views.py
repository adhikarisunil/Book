# books/views.py

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

 

class CustomTokenObtainPairView(TokenObtainPairView):
    pass


class 