import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Account, Destination
from django.shortcuts import render
import requests

@csrf_exempt
def incoming_data(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            data = body  # Get the entire body as data

            if not data:
                return JsonResponse({'error': 'Invalid data format. Data field is missing.'}, status=400)

            app_secret_token = request.headers.get('CL-X-TOKEN')
            if not app_secret_token:
                return JsonResponse({'error': 'Unauthenticated. App secret token is missing.'}, status=401)

            try:
                account = Account.objects.get(app_secret_token=app_secret_token)
            except Account.DoesNotExist:
                return JsonResponse({'error': 'Account not found.'}, status=404)

            for destination in Destination.objects.filter(account=account):
                send_data_to_destination(data, destination)

            return JsonResponse({'message': 'Data received and processed successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint'}, status=405)

def send_data_to_destination(data, destination):
    headers = {}
    for header in destination.headers.all():
        headers[header.key] = header.value

    payload = data

    if destination.http_method == 'GET':
        response = requests.get(destination.url, params=payload, headers=headers)
    elif destination.http_method == 'POST':
        response = requests.post(destination.url, json=payload, headers=headers)
    elif destination.http_method == 'PUT':
        response = requests.put(destination.url, json=payload, headers=headers)
    else:
        raise ValueError(f"Unsupported HTTP method: {destination.http_method}")

    if response.status_code != 200:
        raise ValueError(f"Error sending data to destination {destination.url}: {response.status_code} - {response.text}")

def home(request):
    return render(request, 'data_pusher_app/home.html')
