from django.db import models
from django.conf import settings
from datetime import date
from django.core.validators import EmailValidator

class Recipe(models.Model):
    email = models.EmailField(validators=[EmailValidator()])
    title = models.CharField(max_length=200)
    ingredients = models.TextField()  # You can break this down further if needed
    
    # Nutrient fields
    calories = models.FloatField(default=0)  # kcal
    fat = models.FloatField(default=0)  # g
    saturated_fat = models.FloatField(default=0)  # g
    carbohydrates = models.FloatField(default=0)  # g
    sugar = models.FloatField(default=0)  # g
    cholesterol = models.FloatField(default=0)  # mg
    sodium = models.FloatField(default=0)  # mg
    protein = models.FloatField(default=0)  # g
    
    # Date prepared with default set to today's date
    date_prepared = models.DateField(default=date.today)

    def __str__(self):
        return self.email
