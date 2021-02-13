from django.shortcuts import render

# Create your views here.

def gitpage(request):
    """A view to return index page"""

    return render(request, 'gitpage.html')
