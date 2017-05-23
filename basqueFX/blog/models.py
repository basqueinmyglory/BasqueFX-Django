from django.db import models

# Create your models here.
class Blogpost(models.Model):
    entry_date = models.DateField(blank=True, null=True)
    author = models.CharField(max_length=25, blank=True, null=True)
    subject = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'Blogpost'

    def __str__(self):
        return str(self.entry_date) + " | " + str(self.title) 