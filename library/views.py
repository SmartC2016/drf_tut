# these are only REST API Views
from rest_framework import generics, permissions
from rest_framework.serializers import Serializer
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    # This one adds permissions
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer
    