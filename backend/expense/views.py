from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *

# Create your views here.

#Signup API
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Name = data.get('name')
        Email = data.get('email')
        Password = data.get('password')

        if UserDetails.objects.filter(email=Email).exists():
            return JsonResponse({'status': 'error', 'message': 'Email already exists'}, status=400)
        UserDetails.objects.create(name=Name, email=Email, password=Password)
        return JsonResponse({'status': 'success', 'message': 'User registered successfully'}, status=201)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
        