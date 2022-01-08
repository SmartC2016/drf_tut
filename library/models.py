from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    num_pages = models.IntegerField(default=0)
    published_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=9)
    colour = models.CharField(max_length=100, blank=True, null=True)
    isbn13 = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
