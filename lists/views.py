from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<html><title>To-Do lists</title>hello world</html>")
