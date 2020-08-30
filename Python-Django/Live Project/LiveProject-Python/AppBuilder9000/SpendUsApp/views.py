import datetime                     #used for passing dates in easy to display format
from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense         #import the class of Expense to be able to use object definition
from .forms import ExpenseForm  #import the Expense Form to be able to create and save
#from .api_service import *          #imports the functions from the API Service module created
from django.utils import timezone   #used for converting time from UTC to users time zone
import requests                     #necessary for datascraping
from bs4 import BeautifulSoup as BS #necessary for datascraping

#Function to display home page
def home(request):
    return render(request, "SpendUsApp/spendus_home.html") #render the home page


#View function that controls the main index page - list of expenses
def index(request):
    get_expenses = Expense.Expenses.all()       #Gets all the current expenses from the database
    context = {'expenses': get_expenses}        #Creates a dictionary object of all the expenses for the template
    return render(request, 'SpendUsApp/spendus_index.html', context)


#View function to add a new expense to the database
def add_expense(request):
    form = ExpenseForm(request.POST or None)     #Gets the posted form, if one exists
    if form.is_valid():                         #Checks the form for errors, to make sure it's filled in
        form.save()                             #Saves the valid form/expense to the database
        return redirect('listExpense')          #Redirects to the index page, which is named 'spendus_index' in the urls
    else:
        print(form.errors)                      #Prints any errors for the posted form to the terminal
        form = ExpenseForm()                     #Creates a new blank form
    return render(request, 'SpendUsApp/spendus_create.html', {'form':form})


#View function to look up the details of an Expense
def details_expense(request, pk):
    pk = int(pk)                                #Casts value of pk to an int so it's the proper data type
    expense = get_object_or_404(Expense, pk=pk)   #Gets single instance of the expense from the database
    context={'expense':expense}                   #Creates dictionary object to pass the expense object
    return render(request,'SpendUsApp/spendus_details.html', context)


# View function to edit a expense item
def edit_expense(request, pk):
    #global form
    pk = int(pk)
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid(): #validation
            expense = form.save()
            expense.save()
            return redirect('expenseDetails', pk=expense.pk) #redirects to details page
    else:
        form = ExpenseForm(instance=expense)
    context = {'form': form, 'pk': pk, 'expense': expense.name}
    return render(request, 'SpendUsApp/spendus_edit.html', context) #renders to the edit template using the context and request

#View function to delete expense item
def delete_expense(request, pk): #request not needed because not used
    ex = Expense.Expenses.get(pk=pk) #no request method sent in this function, just accessed using django method querying database
    ex.delete() #calling Django built in method to delete this record in the table
    return redirect('listExpense') #upon delete, return to 'listExpense' page


#View function to scrape recent AP news stories on federal spending
def ap_news_expense(request):
    source = requests.get("https://apnews.com/Governmentspending")     #Get apnews.com/government spending as an html document
    print(source.status_code)                   #Used for debugging to ensure a 'success' code of 200
    soup = BS(source.content, 'html.parser')    #Initial processing of the html by beautiful soup, soup is now a navigatable object
    nodes = soup.find_all(attrs={"data-key": "feed-card-wire-story-with-image"})  # Search for divs with class
    articles = []                               #Create blank array to add articles to
    for node in nodes:                          #Iterates through all the objects with class of node-title
        if node != None:
            title = node.h1.get_text()       #Sets title equal to the text of the h1 tag
            link = node.find('a').get('href')       #Sets link equal to the href of the a tag
            timestamp = node.find('span', attrs={"data-key": "timestamp"}).get_text()   #Uses attribute value timestamp
            url = "https://apnews.com/Governmentspending" + link    #Modifies the link to a full url, since the links were relative
            article={'title':title, 'url': url, 'date': timestamp}  #Creates an article object dictionary with needed elements
            articles.append(article)                #Adds article dictionary item to the array before iterating through next node
        else:
            print('no value')
    context={'articles': articles}              #Creates a dictionary element for the articles to pass to the template
    return render(request, 'SpendUsApp/spendus_news.html', context)


'''def news(request):
    response = requests.get("https://www.dicetowernews.com/")
    content = BeautifulSoup(response.content, "html.parser")

    storyList = []
    stories = content.find_all('div', class_='node-news-article')
    for story in stories:
        h2_tag = story.h2
        story_link = h2_tag.a.get('href')
        story_title = h2_tag.get_text()
        if story.img:
            story_image = story.img.get('src')
        else:
            story_image=""

        new_story = {
            # 'h2_tag': h2_tag,
            'story_link': story_link,
            'story_title': story_title,
            'story_image': story_image
        }

        storyList.append(new_story)
    context = {
        'page': storyList,

    }
    return render(request, "BoardGame/boardgame_news.html", context) '''