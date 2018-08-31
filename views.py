import datetime

from django.http import HttpResponse
from django.template.loader import get_template


def hours_ahead(request, offset):
    futurhour = datetime.datetime.now() + datetime.timedelta(hours=offset)
    datetemplate = get_template('next_date.html')
    dictofcontext = {'hour': offset, 'dt': futurhour}
    html = datetemplate.render(dictofcontext)
    return HttpResponse(html)
