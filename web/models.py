from django.db import models


# Create your models here.
class CronNote(models.Model):
    note = models.DateTimeField(auto_now=True)
