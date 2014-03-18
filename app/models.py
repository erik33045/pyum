from django.db import models
from django.contrib.auth.models import User


class YummlyDiet(models.Model):
    shortDescription = models.CharField(max_length=50)
    longDescription = models.CharField(max_length=1000)
    searchValue = models.CharField(max_length=250)

    def __unicode__(self):
        return self.shortDescription


class AppUser(models.Model):
    user = models.OneToOneField(User)
    yummlydiet = models.ForeignKey(YummlyDiet, default=1)
    picture = models.ImageField(upload_to='profile_images/', blank=True)

    def __unicode__(self):
        return self.user.username