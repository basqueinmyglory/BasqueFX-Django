from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Dailyforecast(models.Model):
    USD = 'USD'
    GBP = 'GBP'
    EUR = 'EUR'
    JPY = 'JPY'
    CAD = 'CAD'
    AUD = 'AUD'
    NZD = 'NZD'
    No_Option = '---'
    CURRENCY_OPTIONS = (
        (USD, 'USD'),
        (GBP, 'GBP'),
        (EUR, 'EUR'),
        (JPY, 'JPY'),
        (CAD, 'CAD'),
        (AUD, 'AUD'),
        (NZD, 'NZD'),
        (No_Option, '---'),
    )
    entry_date = models.DateTimeField(max_length=500)
    strong_cur = models.CharField(max_length=3, choices=CURRENCY_OPTIONS, default=USD)
    strong_reason = RichTextField()
    weak_cur = models.CharField(max_length=3, choices=CURRENCY_OPTIONS, default=USD)
    weak_reason = RichTextField()
    notes = RichTextField()
    
    def __str__(self):
        return str(self.entry_date) + " | Strong: " + str(self.strong_cur) + " | Weak: " + str(self.weak_cur)

class Calevents(models.Model):
    date = models.DateTimeField(max_length=500)  # Field name made lowercase.
    currency = models.CharField(max_length=50)  # Field name made lowercase.
    event = models.CharField(max_length=50)  # Field name made lowercase.
    impact = models.CharField(max_length=50)  # Field name made lowercase.
    time_eastern = models.CharField(max_length=50)  # Field name made lowercase.
    forecast = models.CharField(max_length=50)  # Field name made lowercase.
    previous = models.CharField(max_length=50)  # Field name made lowercase.