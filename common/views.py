from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'common/home.html')


def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'common/about.html')


def contact_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'common/contact.html')

def page_not_found(request, exception):
    return render(request, 'common/404.html', status=404)


