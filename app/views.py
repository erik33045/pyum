from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django_tables2 import RequestConfig

import app.tables
from app.forms import UserForm, AppUserForm
import YummlyDriver


def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = AppUserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = AppUserForm()

    # Render the template depending on the context.
    # noinspection PyUnresolvedReferences
    return render(request, 'app/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return render(request, 'app/home.html', {})
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Pyum account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}".format(username)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        # noinspection PyUnresolvedReferences
        return render(request, 'app/login.html', {})


def search_recipes(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            #pull parameters out of the post object
            parameters = YummlyDriver.django_query_dictionary_to_parameter_object(request.POST)
            #query for the matches
            results = YummlyDriver.search_recipes(parameters).matches
            #map to table data
            table_data = app.tables.map_from_result_list(results)
            table = app.tables.ResultTable(table_data)
            RequestConfig(request).configure(table)
            # noinspection PyUnresolvedReferences
            #render the table
            return render(request, 'recipes.html', {'table': table})
        else:
            return render(request, 'recipes.html', {'table': app.tables.ResultTable([])})
    else:
        return render(request, 'app/login.html', {})


# noinspection PyUnresolvedReferences
def home(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            parameters = YummlyDriver.django_query_dictionary_to_parameter_object(request.POST)
            #Need to put in the rest of the user parameters here if need be

            print search_recipes(request, parameters)
            #need to fire off the call to the recipes page
            return httpResponsRedirect('recipes.htm')

        return render(request, 'app/home.html', {})
    else:
        return render(request, 'app/login.html', {})


def user_logout(request):
    logout(request)
    return render(request, 'app/login.html', {})


def profile(request):
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the the previous section
        form = ProfileForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ProfileForm() # An unbound form

    return render(request, 'profile.html', {
        'form': form,
    })
