from django.shortcuts import render
from django.http import HttpResponse

from .testimonials import testimonials

# Create your views here.
def home(request):
    return render(request,'main/home.html', {'testimonials': testimonials})

def about(request):
    return render(request,'main/about.html')

def contact(request):
    return render(request,'main/contact.html')

def service(request):
    return render(request,'main/services.html')

def ukcollege(request):
    return render(request,'main/ukcollege.html')

def uscollege(request):
    return render(request,'main/uscollege.html')

def cancollege(request):
    return render(request,'main/cancollege.html')

def auscollege(request):
    return render(request,'main/auscollege.html')

def uk_harvard_unversity_detail_view(request):
    return render(request, 'uk_college_detail/harvard University_description.html')

def uk_stanford_unversity_detail_view(request):
    return render(request, 'uk_college_detail/stanford_university_detail.html')

def uk_mit_unversity_detail_view(request):
    return render(request, 'uk_college_detail/MIT_university_detail.html')