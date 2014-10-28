from django.shortcuts import render
from sistema.models import *
from sistema.forms import *

# Create your views here.


def home(request):
    return render(request, 'home.html', locals())
