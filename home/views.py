from django.shortcuts import render


# Displays the home page
def home(request):

    return render(request, 'index.html')
