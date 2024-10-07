from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'user', 'title', 'ingredients', 'calories', 'fat', 'saturated_fat', 'carbohydrates', 'sugar', 'cholesterol', 'sodium', 'protein', 'date_prepared']
