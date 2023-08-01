# books/serializers.py

from rest_framework import serializers
from .models import Book, Nobel, Poem

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class NobelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nobel
        fields = '__all__'

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = '__all__'