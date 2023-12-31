from django.shortcuts import render, get_object_or_404
from .models import Letting
import logging


lettings_logger = logging.getLogger('lettings')


def index(request):
    """
    Display the list of all available lettings.

    :param request: The HTTP request object.
    :return: The rendered page with the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    lettings_logger.info('User accessed the lettings index page')
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Display the details of a specific letting.

    :param request: The HTTP request object.
    :param letting_id: The identifier of the letting to display.
    :return: The rendered page with the details of the letting.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    lettings_logger.info(f'User viewed details for letting ID: {letting_id}')
    return render(request, 'lettings/letting.html', context)
