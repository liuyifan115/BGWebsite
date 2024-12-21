from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=256)

    def set_password(self, password):
        self.password = password

    def __str__(self):
        return self.username