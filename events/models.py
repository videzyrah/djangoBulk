from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Host(models.Model):
    name = models.OneToOneField(User, on_delete = models.PROTECT)

class Potluck(models.Model):
    theme = models.CharField(max_length=200, unique=True)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    facebookPage = models.CharField(max_length=200, blank=True, null=True)
    details = models.TextField(max_length=2000)
    event_date = models.DateField()

    def __str__(self):
        return self.theme
