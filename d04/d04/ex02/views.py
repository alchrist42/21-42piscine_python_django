import logging
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.conf import settings
from .forms import HistoryForm

logging.config.dictConfig(settings.LOGGING_EX02)

def index(request: HttpRequest):
    logger = logging.getLogger('history')

    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data['data'])
        return redirect('/ex02')
    elif request.method == 'GET':
        # print("get_request")
        try:
            f = open(settings.HISTORY_LOG_FILE, 'r')
            data = f.readlines()
        except:
            data = []
        # print(data)

    return render(request, 'ex02/index.html', {'form': HistoryForm(), 'data': data})