from django.shortcuts import render

# Create your views here.

def djangopage(request):
    """A view to return index page"""

    return render(request, 'django.html')
