from django.shortcuts import render


# Displays the home page
def home(request):
    return render(request, 'index.html')


# handle 404 errors
def handle_404(request, exception):
    return render(request, '404.html', {})
