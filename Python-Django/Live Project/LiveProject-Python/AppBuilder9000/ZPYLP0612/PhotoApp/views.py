from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Photography
from .forms import photographyform

# Create your views here.
def home(request):
    return render(request, 'PhotoApp/PhotoApp_home.html')

def index(request):
    get_Photo = Photography.Photography.all()      #Gets all the current photo from the database
    context = {'Photos': get_Photo}      #Creates a dictionary object of all the photo for the template
    return render(request, 'PhotoApp/PhotoApp_index.html',context)

def add_photo(request):
    form = photographyform(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form/photo to the database
        return redirect('PhotoAlbum')                #Redirects to the index page, which is named 'Photo' in the urls
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = photographyform()                     #Creates a new blank form
    return render(request, 'PhotoApp/PhotoApp_create.html', {'form':form})

#View function to look up the photos within that album
def Photo_Album(request, pk):
    pk = int(pk)
    album = get_object_or_404(Photography, pk=pk)   #Gets single photos from the database
    context = {
        'album': album,
    }
    return render(request,'PhotoApp/PhotoApp_details.html',context)