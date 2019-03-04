from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs): # *args, **kwargs
	return HttpResponse("<h1>Hello World</h1>") # string of HTML code


def contact_view(*args, **kwargs): # *args, **kwargs
	return HttpResponse("<h1>Contact Page</h1>")


def about_view(*args, **kwargs): # *args, **kwargs
	return HttpResponse("<h1>About Page</h1>")


def social_view(*args, **kwargs): # *args, **kwargs
	return HttpResponse("<h1>Social Page</h1>")