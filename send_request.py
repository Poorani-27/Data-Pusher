import os
import sys
import requests
import django

# Add project directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_pusher_project.settings")
django.setup()

# Import the Account model
from data_pusher_app.models import Account

def send_post_request():
    # Define the API endpoint and data to send
    api_url = "http://127.0.0.1:8000/api/"
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    
    # Define the app secret token
    app_secret_token = "Your_secert_token"
    
    # Set the headers with the app secret token and other required headers
    headers = {
    
        "APP_SECRET": app_secret_token,
        "ACTION": "user.update",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "CL-X-TOKEN": app_secret_token
    }
    
    try:
        # Check if the account exists in the database
        if not Account.objects.filter(app_secret_token=app_secret_token).exists():
            # If the account does not exist, create and save it
            new_account = Account.objects.create(app_secret_token=app_secret_token, account_name='example_account_name', email='example@example.com')
        
        # Send the POST request
        response = requests.post(api_url, json={"data": data}, headers=headers)  # Wrap 'data' in another dict
        
        # Print the response from the server
        print(response.json())
    
    except Exception as e:
        print("An error occurred:", e)

# Call the function to send the POST request
send_post_request()
