# In your urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('recipes/update-nutrients/', views.update_nutrients, name='update_nutrients'),
    path('download-csv/', views.download_csv, name='download_csv')
]
