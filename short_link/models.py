from django.db import models

class ShortLink(models.Model):
    token = models.CharField(max_length=27)
    link = models.CharField(max_length=2000)

    def __str__(self):
        self.token
