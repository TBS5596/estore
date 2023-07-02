from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return self.user.username