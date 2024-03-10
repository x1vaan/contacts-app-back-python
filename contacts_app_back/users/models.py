from django.db import models
from django.utils.timezone import now

# Create your models here.
class UserTest(models.Model):
    name = models.CharField(max_length=20, null=False)
    username = models.CharField(max_length=20, null=False, unique = True)
    email = models.CharField(max_length=30, null=False, unique = True)
    password = models.CharField(max_length=25, null = False)
    created_at = models.DateTimeField(default= now, editable=False)