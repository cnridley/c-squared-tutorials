from django.shortcuts import render

# Create your views here.
def jspage(request):
    """A view to return index page"""

    return render(request, 'jspage.html')

def jsbasics(request):

    return render(request, 'jsbasics.html')