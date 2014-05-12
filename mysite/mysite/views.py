from django.http import Http404, HttpResponse
import datetime
from django.shortcuts import render

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('curr_datetime.html')
    #html = t.render(Context({'current_date': now}))
    return render(request, 'curr_datetime.html', {'current_date': now})

def hello(request):
    return HttpResponse("Hello world")
    
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, "offset_date.html", {'offset': offset, 'date': dt })