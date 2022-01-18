from django.db import models
from django.urls import reverse

# Models
class Condition(models.Model):
    quality = models.CharField(max_length=100)
    
    def __str__(self):
        return self.quality
    
    def get_absolute_url(self):
        return reverse('conditions_detail', kwargs={'pk': self.id})

class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    size = models.IntegerField()
    price = models.IntegerField()
    conditions = models.ManyToManyField(Condition)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sneaker_id': self.id})

class Resale(models.Model):
    date = models.DateField('resale date')
    price = models.IntegerField()
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)

    def __str__(self):
        return F"Date: {self.date} <br> Resale Price: {self.price}"
    
    class Meta:
        ordering = ['date'] 