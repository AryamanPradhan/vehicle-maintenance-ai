from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    middle_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length = 10)

    def __str__(self):
        return self.user.email