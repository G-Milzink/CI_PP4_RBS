from django.shortcuts import render


# Displays the home page
def home(request):
    return render(request, 'index.html')


def handle_404(request, exception):
    return render(request, '404.html', {})
