from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        if email == 'test@test.com' and password == '1234':
            return JsonResponse({
                'access':'dummy-jwt-token'
            })
        
        return JsonResponse({
            'error':'Invalid credentials'
        })
    
    return JsonResponse(
        {'error': 'POST required'},
        status=405
    )  