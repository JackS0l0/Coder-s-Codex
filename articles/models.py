from django.db import models
from django.utils import timezone
class Topadvertising(models.Model):
    txt=models.TextField('txt')
    def __str__(self):
        return self.txt
    class Meta:
        verbose_name = 'Advertising'
        verbose_name_plural = 'Advertising'
class Trend(models.Model):
    txt=models.TextField('txt')
    date=models.DateTimeField('Date',default=timezone.now)
    def __str__(self):
        return self.txt
    class Meta:
        verbose_name = 'Trend'
        verbose_name_plural = 'Trends'