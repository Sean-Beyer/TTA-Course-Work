from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Comedies
from .forms import ComedyForm


# Create your views here.


#View function that renders the home page, no context needed.
def home(request):
    return render(request, 'GreatestComedies/GreatestComedies_home.html')

#View function that controls the main index page - list of jerseys
def index(request):
    get_comedy = Comedies.Comedy.all()      #Gets all the current Comedies from the database
    context = {'comedy': get_comedy}      #Creates a dictionary object of all the comedies in the template
    return render(request, 'GreatestComedies/GreatestComedies_index.html', context)



#View function to add a new comedy to the database
def add_comedy(request):
    form = ComedyForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid Comedy request to the database
        return redirect('listComedy')
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = ComedyForm()                     #Creates a new blank form
        return render(request, 'GreatestComedies/GreatestComedies_create.html', {'form':form})

#View function to look up the details of a comedy
def details_comedy(request, pk):
    pk = int(pk)                                    #Casts value of pk to an int so it's in the proper form
    comedy = get_object_or_404 (Comedies, pk=pk)      #Gets single Comedy from the database
    context = {'Comedies':comedy}                         #Creates dictionary object to pass the Comedy
    return render(request,'GreatestComedies/GreatestComedies_details.html', context)