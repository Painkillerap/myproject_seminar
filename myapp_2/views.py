# Create your views here.
import datetime
import logging
from random import choice

from django.http import HttpResponse

from myapp_2.models import Coin

logger = logging.getLogger(__name__)


def index(request):
    title = "<h2>Вы находитесь на главной странице</h2>"
    logger.info(f'Посещение главной страницы - {datetime.datetime.now()}')
    return HttpResponse(title)


def coin(request):
    result = choice(['Решка', 'Орел'])
    orl_or_resh = Coin(result=result)
    orl_or_resh.save()
    logger.info(f'{orl_or_resh} - {datetime.datetime.now()}')
    return HttpResponse(str(result))


# def statistics(request):

