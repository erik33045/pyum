from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django_tables2 import RequestConfig

import app.tables
from app.forms import UserForm, AppUserForm
from app.models import AppUser
from django.contrib.auth.models import User
import YummlyDriver


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = AppUserForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = AppUserForm()

    return render(request, 'app/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'app/home.html', {})
            else:
                return HttpResponse("Your Pyum account is disabled.")
        else:
            print "Invalid login details: {0}".format(username)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'app/login.html', {})


def search_recipes(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            #Create Parameter Query for Yummly API
            parameters = YummlyDriver.django_query_to_parameter_object(request.POST, request.user.appuser)
            # query for the matches
            results = YummlyDriver.search_recipes(parameters).matches
            #map to table data and store in session
            request.session['results'] = results

        if not request.session.has_key('results'):
            return render(request, 'recipes.html', {'table': app.tables.ResultTable([])})

        result_data = list(request.session['results'])
        table_data = app.tables.map_from_result_list(result_data)
        table = app.tables.ResultTable(table_data)
        RequestConfig(request).configure(table)
        return render(request, 'recipes.html', {'table': table})
    else:
        return render(request, 'app/login.html', {})


# noinspection PyUnresolvedReferences
def home(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            return httpResponsRedirect('recipes.html')

        return render(request, 'app/home.html', {})
    else:
        return render(request, 'app/login.html', {})

def user_logout(request):
    logout(request)
    return render(request, 'app/login.html', {})
