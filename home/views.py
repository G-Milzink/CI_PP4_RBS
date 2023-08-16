# Third party imports:
from django.shortcuts import render


# Displays the home page
def home(request):
    """
    view to display the homepage
    """
    return render(request, 'index.html')


# handle 404 errors
def handle_404(request, exception):
    """
    a view to display the 404 page
    """
    return render(request, '404.html', {})
