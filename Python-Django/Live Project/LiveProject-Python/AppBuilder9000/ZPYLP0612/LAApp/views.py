from django.shortcuts import render, redirect, get_object_or_404
from .models import Author
from .forms import AuthorForm
import requests
from bs4 import BeautifulSoup as BS
import string

#this view renders the home page
def home(request):
    return render(request, 'LAApp/laapp_home.html')

#function that controls the main index page and lists the authors
def index(request):
    get_authors = Author.Authors.all()
    context = {'authors':get_authors}
    return render(request, 'LAApp/laapp_index.html', context)

#function that adds a new author entry to the database
def add_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listAuthors')
    else:
        print(form.errors)
        form = AuthorForm()
    return render(request, 'LAApp/laapp_create.html', {'form':form})

#function to identify listed details of an author
def details_author(request,pk):
    pk = int(pk)
    author = get_object_or_404(Author, pk=pk)
    context={'author':author}
    return render(request,'LAApp/laapp_details.html', context)

def edit_author(request, pk):
    pk=int(pk)
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            author = form.save()
            author.save()
            return redirect('authorDetails', pk=author.pk)
    else:
        form = AuthorForm(instance=author)
    context={'form':form, 'pk':pk}
    return render(request, 'LAApp/laapp_edit.html', context)


def delete(request, pk):
    pk = int(pk)
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('listAuthors')
    context = {'author': author, 'pk':pk}
    return render(request, 'LAApp/laapp_confirm.html', context)

# for beautiful soup and datascraping
def data_Scrape(request):
    source = requests.get("https://en.wikipedia.org/wiki/List_of_science_fiction_authors")
    #print(source.status_code) #code 200 = successful request made
    soup = BS(source.content, 'html.parser')
    # create dropdown menu of first letter in last name and display
    #list of authors from full list of datascraping
    #default set to none upon loading page, then user selects list depending on letter
    w_authors = []  # set a blank array to hold science fiction authors
    alphabetchoices = list(string.ascii_uppercase) # upper case alphabet list to correspond to wikipedia tags
    for letter in alphabetchoices: #loop through each alphabet letter Wikipedia id tag for datascrape
        try: # loop through all existing letters, skip null data
            author_letter = soup.find(id=letter)
            author_biodata = author_letter.find_next('ul').find_all('li') # all data with tag id of letter
            for author in author_biodata: #for each person, to separate out data
                all_author_info = author.get_text() # list each person's data
                first_info_split = all_author_info.split(" (", 1) # split names from first parenthesis, in seperate lists
                authors_name = first_info_split[0] # take elements from first split from above directions
                try: # loop through in case of null data, skip
                    second_info_split = first_info_split[1] #take the second indecises of the first split
                    second_split = second_info_split.rsplit(")", 2) # remove data after the second parenthesis if present
                    years = second_split[0] # take the first index of resulting lists above
                    other = second_split[1] # if there is any data left over, list it here
                    try: # loop through in case of null data, skip
                        link = author.find('a').get('href') # seperate the href associated with each other
                        url = "https://en.wikipedia.org/" + link # join the href to the article link
                        #combine all elements:
                        w_author = {'letter': letter, 'authors_name': authors_name, 'years': years, 'other': other, 'url': url}
                        #save all sorted information to the original list
                        w_authors.append(w_author)
                    except Exception: #skip if no href present
                        pass #continue through without breaking
                except Exception: #skip if no date data
                    pass #continue through without breaking
        except Exception: # to pass over letters with DataType: none
            pass #continue through without breaking
    #print(w_authors) #in case someone wants to see the parsed web-scraped data
    #provide separate alphabet list for dropdown menu, all authors have associated letter for ease of referral in template
    context={"alphabetchoices": alphabetchoices, 'w_authors':w_authors}
    #print(context) #in case you wanted to
    return render(request, 'LAApp/laapp_fanauth.html', context)

#for OpenLibrary API story
def OpenLib_API (request):
    if request.method == 'GET':
        return render(request, 'LAApp/laapp_api_page.html')
    elif request.method =="POST":
        isbn_value = request.POST['search_value']
        if isbn_value != "":
            try:
                user_ISBN = "http://openlibrary.org/api/books?bibkeys=ISBN:" + isbn_value + "&jscmd=data&format=json"
                response = requests.get(user_ISBN)
                #for books API from Open Library

                #print(response.status_code) #code 200 = successful request made for debugging
                #print(response.headers) #'Content-Type': 'application/json'
                data = response.json()
                book_ISBN = 'ISBN:' + isbn_value

                context={'selected_publication' : []}

                subject_types = []
                for subject in data[book_ISBN]['subjects']:
                    subject_list = subject['name']
                    subject_types.append(subject_list)

                try:
                    lrg_image= data[book_ISBN]['cover']['medium']
                except:
                    lrg_image = 'images/app-images/Laapp_butterfly_home.jpg'

                book={
                #print(type(data)) # <class 'dict'>
                #print(data[book_ISBN])
                #print(data.values())
                #print(data[book_ISBN].keys())
                #ALL keys:
                #print(data[book_ISBN]['publishers'])#list:publisher name
                'publish_name' : data[book_ISBN]['publishers'][-1]['name'],
                #print(data[book_ISBN]['pagination'])#str, #of pages
                #print(data[book_ISBN]['identifiers'].keys())#dict
                #print(data[book_ISBN]['identifiers']['isbn_13'])#list, 1 item
                #print(data[book_ISBN]['identifiers']['openlibrary'])#list,1 item
                #print(data[book_ISBN]['identifiers']['isbn_10'])#list, 1 item
                #print(data[book_ISBN]['identifiers']['oclc'])#list,1 item
                #print(data[book_ISBN]['classifications'].keys())#dict
                #print(data[book_ISBN]['classifications']['dewey_decimal_class'])#list, 1 item
                #print(data[book_ISBN]['classifications']['lc_classifications'])#list, 1 item, multiple components
                #print(data[book_ISBN]['title'])#str, title of publication
                'title' : data[book_ISBN]['title'],
                #print(data[book_ISBN]['url'])#str, url of publication
                'link_book' : data[book_ISBN]['url'],
                #print(data[book_ISBN]['number_of_pages'])# int of pages
                'num_pages' : data[book_ISBN]['number_of_pages'],
                #print(data[book_ISBN]['cover'].keys())#dict
                #print(data[book_ISBN]['cover']['small'])#str, url to jpg, depending on size of cover needed
                #print(data[book_ISBN]['cover']['medium'])
                #print(data[book_ISBN]['cover']['large'])
                'lrg_image' : lrg_image,
                #print(data[book_ISBN]['subjects'])#list, urls depending on associated subject types
                'subject_types': subject_types,
                #print(data[book_ISBN]['publish_date'])#str, date however given
                #print(data[book_ISBN]['key']) #str, url to locate in library db
                #print(data[book_ISBN]['authors'])#list url to author, author name
                'author_name' : data[book_ISBN]['authors'][-1]['name'],
                #print(data[book_ISBN]['by_statement']) #str, listed author
                #print(data[book_ISBN]['publish_places'])#list, poss dict of publishers location
                #print(data[book_ISBN]['ebooks']) #list, includes poss dict of preview_url
                }
                context['selected_publication'].append(book)
                #print(book)
                return render(request, 'LAApp/laapp_api_page.html', context)
            except:
                msg = "Sorry, this ISBN is not available in this database, please try again."
                context = {'msg': msg}
                return render(request, 'LAApp/laapp_api_page.html', context)

