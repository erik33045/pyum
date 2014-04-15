from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django_tables2 import RequestConfig
from django.contrib.auth.models import User

import app.tables
from app.forms import UserForm, UserFormWithoutLogin, AppUserForm, RecipeSearchForm
from app.models import AppUser
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


def search_for_recipes(request):
    # Create Parameter Query for Yummly API
    parameters = YummlyDriver.django_query_to_parameter_object(request.POST, request.user.appuser)
    # query for the matches
    results = YummlyDriver.search_recipes(parameters).matches
    #map to table data and store in session
    request.session['results'] = results


def bind_data_to_table(request):
    result_data = list(request.session['results'])
    table_data = app.tables.map_from_result_list(result_data)
    table = app.tables.ResultTable(table_data)
    RequestConfig(request).configure(table)
    return table


def search_recipes(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            search_for_recipes(request)

        search_form = RecipeSearchForm(initial=request.GET)

        table = []
        if not request.session.has_key('results'):
            table = app.tables.ResultTable([])
        else:
            table = bind_data_to_table(request)

        return render(request, 'recipes.html', {'table': table, 'search_form': search_form})
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


def save_user(request):
    post_data = request.POST
    if request.POST['password'] == "":
        post_data['password'] = request.user.password

    user_form = UserFormWithoutLogin(data=post_data, instance=User.objects.get(pk=request.user.id))
    profile_form = AppUserForm(data=post_data, instance=AppUser.objects.get(pk=request.user.appuser.id))

    if user_form.is_valid() and profile_form.is_valid():
        user = user_form.save()
        user.set_password(user.password)
        user.save()
        profile = profile_form.save()
        profile.save()
    return profile_form, user_form


def get_data_for_user(request):
    initial_user_data = {'email': request.user.email}
    initial_app_user_data = {
        'yummlydiet': request.user.appuser.yummlydiet,
        'allergies': request.user.appuser.allergies.all(),
        'age': request.user.appuser.age,
        'gender': request.user.appuser.gender,
        'height': request.user.appuser.height,
        'diabetic': request.user.appuser.diabetic,
        'activity_level': request.user.appuser.activity_level,
        'goal': request.user.appuser.goal}
    user_form = UserFormWithoutLogin(initial=initial_user_data)
    profile_form = AppUserForm(initial=initial_app_user_data)
    return profile_form, user_form


def profile(request):
    if not request.user.is_authenticated():
        return render(request, 'app/login.html', {})

    user_form = UserFormWithoutLogin()
    profile_form = AppUserForm()

    if request.method == 'POST':
        profile_form, user_form = save_user(request)
    else:
        profile_form, user_form = get_data_for_user(request)

    return render(request, 'app/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })