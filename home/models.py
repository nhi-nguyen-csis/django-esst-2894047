from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField() # TextField does not have max length limitation
    created = models.DateField(auto_now_add=True)