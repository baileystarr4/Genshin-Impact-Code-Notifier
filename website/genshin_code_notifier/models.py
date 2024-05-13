from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    carrier = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_number

class Code(models.Model):
    link = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link