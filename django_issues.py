import datetime

from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])  # Not Sensitive?????
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is is is %s.</body></html>" % now
    x = 1
    return HttpResponse(html)
