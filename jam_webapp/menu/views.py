from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main_menu(request):
    return render(request, 'menu/main_menu.html', {})

