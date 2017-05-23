from django.db import models

# Create your models here.

class Dailyforecast(models.Model):
    USD = 'USD'
    GBP = 'GBP'
    EUR = 'EUR'
    JPY = 'JPY'
    CAD = 'CAD'
    AUD = 'AUD'
    NZD = 'NZD'
    CURRENCY_OPTIONS = (
        (USD, 'USD'),
        (GBP, 'GBP'),
        (EUR, 'EUR'),
        (JPY, 'JPY'),
        (CAD, 'CAD'),
        (AUD, 'AUD'),
        (NZD, 'NZD'),
    )
    pub_date = models.DateTimeField(max_length=500)
    strong_cur = models.CharField(max_length=3, choices=CURRENCY_OPTIONS, default=USD)
    strong_reason = models.TextField(max_length=500)
    weak_cur = models.CharField(max_length=3, choices=CURRENCY_OPTIONS, default=USD)
    weak_reason = models.TextField(max_length=500)
    notes = models.TextField(max_length=500)
    
    def __str__(self):
        return str(self.pub_date) + " | Strong: " + str(self.strong_cur) + " | Weak: " + str(self.weak_cur)