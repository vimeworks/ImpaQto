from django.db import models
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='profiles',blank=True,null=True)
    
    def __str__(self):
        return self.user.username
