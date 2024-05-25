# data_pusher_app/management/commands/send_post_request.py

from django.core.management.base import BaseCommand
from data_pusher_app.models import Account
import requests

class Command(BaseCommand):
    help = 'Sends a POST request to the API'

    def handle(self, *args, **options):
        # Define the API endpoint and data to send
        api_url = "http://127.0.0.1:8000/api/"
        data = {
            "key1": "value1",
            "key2": "value2"
        }
        
        # Define the app secret token
        app_secret_token = "AIzaSyDw1mnnGsaojAPWzWSO-NUm60E8fp3Derw"
        
        # Set the headers with the app secret token and other required headers
        headers = {
            "APP_ID": "1234APPID1234",
            "APP_SECTET": "enwdj3bshwer43bjhjs9ereuinkjcnsiurew8s",
            "ACTION": "user.update",
            "Content-Type": "application/json",
            "Accept": "*",
            "CL-X-TOKEN": app_secret_token
        }
        
        try:
            # Check if the account exists in the database
            if not Account.objects.filter(app_secret_token=app_secret_token).exists():
                # If the account does not exist, create and save it
                new_account = Account.objects.create(app_secret_token=app_secret_token, username='poorani', email='tpoorani2002@gmail.com')
            
            # Send the POST request
            response = requests.post(api_url, json=data, headers=headers)
            
            # Print the response from the server
            self.stdout.write(self.style.SUCCESS(response.json()))
        
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))
