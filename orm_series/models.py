from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.core.exceptions import ValidationError
def val_startswith_a(value):
    if not value.startswith('a'):
        raise ValidationError('This is Custom Validator')

class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN','Indian'
        CHINESE = 'CH','Chinese'
        ARABIAN = 'AR','Arabian'
        MEXICAN = 'MX','Mexican'
        OTHER = 'OT','Other'
        
    name = models.CharField(max_length=100)
    website = models.URLField(null=True)
    date_opened = models.DateField()
    latitude = models.FloatField(validators=[MinValueValidator(-90),MaxValueValidator(90)])
    longitude = models.FloatField(validators=[MinValueValidator(-180),MaxValueValidator(180)])
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices)

class Staff(models.Model):
    name = models.CharField(max_length=20)
    restaurants = models.ManyToManyField(Restaurant)
    
    def __str__(self):
        return self.name
    
class Sales(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL,null=True)
    income = models.DecimalField(max_digits=8,decimal_places=2)
    date_time = models.DateTimeField()
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    