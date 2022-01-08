from django.db import models
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "num_pages",
            "published_date",
            "price",
            "colour",
            "isbn13",            
        ]
        # For the data fields which are not "required" and therefor
        # it can happen, that they will not be given
        extra_kwargs = {
            "published_date": {"required": False},
            "price": {"required": False},
            "colour": {"required": False},
            "isbn13": {"required": False},
        }
