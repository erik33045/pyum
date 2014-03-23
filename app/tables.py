# tutorial/tables.py
import django_tables2 as tables

from app.models import AppUser


class UserTable(tables.Table):
    class Meta:
        model = AppUser
        # add class="paleblue" to <table> tag
