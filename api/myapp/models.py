from django.db import models


# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=10)

    def __str(self):
        return self.name

