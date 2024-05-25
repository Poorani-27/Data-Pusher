from django.db import models
import json

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.CharField(max_length=50, unique=True)
    account_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='default_username')
    app_secret_token = models.CharField(max_length=100, unique=True)
    website = models.URLField(blank=True)

class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    url = models.URLField()
    http_method = models.CharField(max_length=10)
    headers = models.TextField()  # Change JSONField to TextField

    def get_headers(self):
        return json.loads(self.headers)  # Deserialize JSON data when getting headers

    def set_headers(self, headers):
        self.headers = json.dumps(headers)  # Serialize JSON data when setting headers

    data = property(get_headers, set_headers)  # Property to access headers as JSON data
