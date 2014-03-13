from django.db import models
from django.contrib.auth.models import User


class AppUser(models.Model):
    user = models.OneToOneField(User)
    is_vegetarian = models.BooleanField(default=False)
    is_diabetic = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='profile_images/', blank=True)

    def __unicode__(self):
        return self.user.username