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
    entry_date = models.DateTimeField(max_length=500)
    strong_cur = models.CharField(max_length=3, choices=CURRENCY_OPTIONS, default=USD)
    strong_reason = models.TextField(max_length=500)
    weak_cur = models.CharField(max_length=3, choices=CURRENCY_OPTIONS, default=USD)
    weak_reason = models.TextField(max_length=500)
    notes = models.TextField(max_length=500)
    
    def __str__(self):
        return str(self.entry_date) + " | Strong: " + str(self.strong_cur) + " | Weak: " + str(self.weak_cur)

class Events(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    currency = models.TextField(db_column='Currency', blank=True, null=True)  # Field name made lowercase.
    event = models.TextField(db_column='Event', blank=True, null=True)  # Field name made lowercase.
    impact = models.TextField(db_column='Impact', blank=True, null=True)  # Field name made lowercase.
    time_eastern = models.TextField(db_column='Time_Eastern', blank=True, null=True)  # Field name made lowercase.
    forecast = models.TextField(db_column='Forecast', blank=True, null=True)  # Field name made lowercase.
    previous = models.TextField(db_column='Previous', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'events'