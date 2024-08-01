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
class Categories(models.Model):
    name=models.CharField('Name',max_length=200)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
class Article(models.Model):
    name=models.CharField('Name',max_length=200)
    img=models.URLField('Image',default='')
    category = models.ForeignKey(to=Categories,on_delete=models.CASCADE)
    date=models.DateTimeField('Date',default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'