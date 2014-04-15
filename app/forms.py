from django import forms
from django.contrib.auth.models import User

from app.models import AppUser


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserFormWithoutLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password')


class AppUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppUserForm, self).__init__(*args, **kwargs)
        self.fields['height'].label = "Height (inches)"
        self.fields['yummlydiet'].label = "Dietary Restriction"

    class Meta:
        model = AppUser
        fields = ('yummlydiet', 'allergies', 'age', 'gender', 'height', 'diabetic', 'activity_level', 'goal')


class RecipeSearchForm(forms.Form):
    ignore_user_preferences = forms.BooleanField()
    current_weight = forms.IntegerField()
    calories_consumed = forms.IntegerField()
    num_meals = forms.ChoiceField(choices=[(x, x) for x in range(1, 6)])
    in_ingredients = forms.CharField()
    ex_ingredients = forms.CharField()
    prep_time = forms.IntegerField()
