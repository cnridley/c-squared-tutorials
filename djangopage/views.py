from django.shortcuts import render
from .models import PdfUpload

# Create your views here.

def djangopage(request):
    """A view to return index page"""

    Pdf = PdfUpload.objects.all()

    context = {
        'Pdf': Pdf,
    }

    return render(request, 'django.html', context)

def setting_up(request):

    return render(request, 'setting_up.html')