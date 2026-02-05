from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_acknowledged = models.BooleanField(default=False)

    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.message[:50]
