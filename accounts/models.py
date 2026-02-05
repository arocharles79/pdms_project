from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Shift(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username
