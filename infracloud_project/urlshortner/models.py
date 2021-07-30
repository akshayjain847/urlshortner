from django.db import models

# Create your models here.
class UrlData(models.Model):
    url = models.CharField(max_length=200, primary_key=True)
    encode = models.CharField(max_length=70)
    def __str__(self):
            return f"Short Url for: {self.url} is {self.encode}"

class MaxStoreid(models.Model):
    max_id = models.IntegerField(primary_key=True)
        