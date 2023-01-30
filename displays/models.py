from django.db import models

# Create your models here.

class DisplayModel(models.Model):

    model = models.CharField(max_length=50)

    def __str__(self):
        return self.model
