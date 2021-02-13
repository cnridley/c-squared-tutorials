from django.shortcuts import render

# Create your views here.

def csspage(request):
    """A view to return index page"""

    return render(request, 'csspage.html')