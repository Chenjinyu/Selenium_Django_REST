from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def new_conf(request):
    return render(request, 'choose_prod.html')

def proliant_dl_server(request):
    return render(request, 'proliant_dl_server.html')

def configuration_page(request):
    return render(request, 'config_page.html')

