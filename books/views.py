from rest_framework import viewsets
from .models import Book, Nobel, Poem, Post
from .serializers import BookSerializer, NobelSerializer, PoemSerializer, PostSerializer
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

class  PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']

class  NobelViewSet(viewsets.ModelViewSet):
    queryset = Nobel.objects.all()
    serializer_class = NobelSerializer  
    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']  

class  PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']

class CustomTokenObtainPairView(TokenObtainPairView):
    pass
