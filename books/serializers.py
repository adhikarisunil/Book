# books/serializers.py

from rest_framework import serializers
from .models import Book, Nobel

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class NobelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nobel
        fields = '__all__'