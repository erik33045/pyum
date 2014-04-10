from django.db import models
from django.contrib.auth.models import User


class YummlyDiet(models.Model):
    shortDescription = models.CharField(max_length=50, default="DEFAULT")
    searchValue = models.CharField(max_length=250, default="DEFAULT")

    def __unicode__(self):
        return self.shortDescription


class YummlyAllergy(models.Model):
    shortDescription = models.CharField(max_length=50, default="DEFAULT")
    searchValue = models.CharField(max_length=250, default="DEFAULT")

    def __unicode__(self):
        return self.shortDescription


class ActivityLevel(models.Model):
    level = models.CharField(max_length=250)

    def __unicode__(self):
        return self.level

class Goal(models.Model):
    goal = models.CharField(max_length=250)

    def __unicode__(self):
        return self.goal


class AppUser(models.Model):
    user = models.OneToOneField(User)
    yummlydiet = models.ForeignKey(YummlyDiet, default=1)
    allergies = models.ManyToManyField(YummlyAllergy)
    age = models.IntegerField()
    height = models.IntegerField()
    activity_level = models.ForeignKey(ActivityLevel, default=1)
    goal = models.ForeignKey(Goal, default=5)

    def __unicode__(self):
        return self.user.username

