# models.py Defines your database structure
from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField() # TextField does not have max length limitation
    likes = models.PositiveSmallIntegerField(default=0)
    created = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.title}"