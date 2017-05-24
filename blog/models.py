from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    pub_date = models.DateField(blank=True, null=True)
    author = models.CharField(max_length=25, blank=True, null=True)    
    notes = models.TextField()


    def __str__(self):
        return str(self.pub_date) + " | " + str(self.title) 