from django.db import models

# Create your models here.
class Person(models.Model):
    document_type = models.CharField(max_length=100)
    document = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    hobbie = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)