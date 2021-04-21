from django.shortcuts import render # pylint: disable=import-error
from django.http import HttpResponse # pylint: disable=import-error
# Create your views here.
def index(request):
    return HttpResponse("Yayyyyyyy")