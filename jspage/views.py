from django.shortcuts import render

# Create your views here.
def jspage(request):
    """A view to return index page"""

    return render(request, 'jspage.html')


def jsbasics(request):

    return render(request, 'jsbasics.html')


def stringmethods(request):

    return render(request, 'stringmethods.html')

def mathmethods(request):

    return render(request, 'mathmethods.html')


def js_arrays(request):

    return render(request, 'js_arrays.html')