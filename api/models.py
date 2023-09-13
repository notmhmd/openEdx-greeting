from django.db import models


class Greeting(models.Model):
    text = models.TextField()
