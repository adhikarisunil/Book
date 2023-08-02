from rest_framework import serializers
from .models import Book, Nobel, Poem, UserProfile, Post
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_title(self, value):
        # Add your custom validation logic for the title field here.
        # For example, you can check for a specific pattern or length.
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value
    
    def validate_publication_date(self, value):
        # Add your custom validation logic for the publication_date field here.
        # For example, you can check if the date is in the past or not.
        from datetime import date
        if value > date.today():
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return value

class NobelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nobel
        fields = '__all__'

class PoemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poem
        fields = '__all__'