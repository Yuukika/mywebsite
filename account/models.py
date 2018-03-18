from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,unique=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return 'user {}'.format(self.user.username)

