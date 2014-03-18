from django.contrib import admin

from app.models import AppUser
from app.models import YummlyDiet


# Register your models here.
admin.site.register(AppUser)
admin.site.register(YummlyDiet)