from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='spend_us'),                  #URL for home of the SpendUsApp
    path('Collection/', views.index, name='listExpense'),   #Index of expenses
    path('AddToCollection/', views.add_expense, name='createExpense'), # add new expense
    path('Collection/<int:pk>/Details/', views.details_expense, name='expenseDetails'), # get details for a single expense
    path('Collection/<int:pk>/Edit/', views.edit_expense, name="edit"), #Edit functionality gets its own page
    path('Collection/<int:pk>/Edit/Delete/', views.delete_expense, name="delete"), #Delete function accessed via modal on edit page
    path('SpendNews/', views.ap_news_expense, name='spendNews'),       #Data scraped news from AP website on gov spending
]