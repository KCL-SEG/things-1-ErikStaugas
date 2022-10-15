from email.policy import HTTP
from urllib import response
from django.shortcuts import render

# Django creates and object of all the information it received in a HTTP request.
def home(request):
    return render(request, 'things.html')