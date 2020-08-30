from django.shortcuts import render


def index(request):  # temporary homepage view
    return render(request, 'EarningsApp/earningsapp_index.html')
