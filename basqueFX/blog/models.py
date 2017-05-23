from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(max_length=500)
    author = models.CharField(max_length=25)
    notes = models.TextField()
