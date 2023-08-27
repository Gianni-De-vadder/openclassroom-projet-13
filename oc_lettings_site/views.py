from django.shortcuts import render
from django.http import HttpResponse
import logging

lettings_logger = logging.getLogger('lettings')
profiles_logger = logging.getLogger('profiles')

def index(request):
    lettings_logger.error('Mega erreur')
    return render(request, 'index.html')

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

def custom_500(request, exception=None):
    return render(request, '500.html', status=500)

