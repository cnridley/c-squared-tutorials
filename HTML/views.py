from django.shortcuts import render

# Create your views here.

def htmlpage(request):
    """A view to return index page"""

    return render(request, 'htmlpage.html')