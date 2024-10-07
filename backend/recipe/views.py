from django.http import JsonResponse
from .models import Recipe
from django.views.decorators.csrf import csrf_exempt
import json
import re
import csv
import os
from io import StringIO
from django.conf import settings
from .models import Recipe # Import your model
from django.http import HttpResponse, Http404
from django.contrib.auth import get_user_model


# Helper function to strip units and convert to float
user_email=""
@csrf_exempt
def update_nutrients(request):
    global user_email
    if request.method == 'POST':
        try:
            # Load and parse the JSON data from the request
            data = json.loads(request.body)

            # Extract fields from the JSON data
            title = data.get('title')
            ingredients = data.get('ingredients', '')  # Ensure ingredients is a string
            nutrients = data.get('nutrients', [])
            print(data)
            print(data['email'])
            print(data['title'])
            print("o")
            print("Nutrient Values:")
            print("Calories:", re.sub(r'\D', '', data['calories']))
            print("Fat:", re.sub(r'\D', '', data['fat']))
            print("Saturated Fat:", re.sub(r'\D', '', data['saturated_fat']))
            print("Carbohydrates:", re.sub(r'\D', '', data['carbohydrates']))
            print("Sugar:", re.sub(r'\D', '', data['sugar']))
            print("Cholesterol:",re.sub(r'\D', '', data['cholestrol']))
            print("Sodium:",re.sub(r'\D', '', data['sodium']))
            print("Protein:",re.sub(r'\D', '', data['protein']))

            user_email=data['email']

            # Check if the user is authenticated

            # Create a new recipe instance with cleaned nutrient data
            recipe = Recipe.objects.create(
                email=data['email'],
                title=data['title'],
                ingredients=",  ".join(data['ingredients']),  # Now it's ensured as a string
                calories= re.sub(r'\D', '', data['calories']),
                fat= re.sub(r'\D', '', data['fat']),
                saturated_fat=re.sub(r'\D', '', data['saturated_fat']),
                carbohydrates=re.sub(r'\D', '', data['carbohydrates']),
                sugar=re.sub(r'\D', '', data['sugar']),
                cholesterol=re.sub(r'\D', '', data['cholestrol']),
                sodium=re.sub(r'\D', '', data['sodium']),
                protein=re.sub(r'\D', '', data['protein']),
            )
            print(recipe.id)

            return JsonResponse({'status': 'success', 'recipe_id': recipe.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def generate_csv(request, email):
    # User = get_user_model()
    # try:
    #     user = User.objects.get(email=email)
    # except User.DoesNotExist:
    #     return HttpResponse("User not found", status=404)

    # Create a HttpResponse object with CSV header
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{email}_data.csv"'

    # Create a CSV writer object
    writer = csv.writer(response)

    # Write the header row
    fields = [field.name for field in Recipe._meta.fields]
    writer.writerow(fields)

    # Get records for the specific user
    records = Recipe.objects.all()  # Adjust this filter based on your model structure

    # Write data rows
    for record in records:
        if record.email==email:
            writer.writerow([getattr(record, field) for field in fields])

    return response

def download_csv(request):
    email = request.GET.get('email')
    print(email)
    if not email:
        return HttpResponse("Email parameter is required", status=400)
    
    try:
        return generate_csv(request, email)
    except Exception as e:
        # If an error occurs, log it and return an error response
        print(f"Error generating CSV: {str(e)}")
        return HttpResponse("An error occurred while generating the CSV file.", status=500)