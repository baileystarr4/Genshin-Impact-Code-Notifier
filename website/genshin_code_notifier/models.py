from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True,null=True, blank=True)

    def __str__(self):
        return self.email

class Code(models.Model):
    link = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link