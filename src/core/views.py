from django.shortcuts import render
import logging
# Create your views here.

logger = logging.getLogger('django')


def home(request):
    logger.warning('request is processing')
    return render(request, 'main/home.html', {'user': request.user})
