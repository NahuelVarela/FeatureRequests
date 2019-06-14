from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.models import User

#Our project imports
from .models import FeaturesItems
from .forms import FeaturesForm

# Create your views here.
def index(request):
    return render(request,"index.html")

def auth_page(request):
    return render(request,"auth_page.html")

def feature_request_form(request):
	#This view will handle the creation of Features request.
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FeaturesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            obj_features, created = FeaturesItems.objects.update_or_create(
            	owner= request.user.username,
            	title= form.cleaned_data["title"],
            	description= form.cleaned_data["description"]
            	)

            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FeaturesForm()

    return render(request, 'fr_form.html', {'form': form})
