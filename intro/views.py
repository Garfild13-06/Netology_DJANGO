import datetime

from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
# MVC - Model-View-Controller
# MTV - Model-Template-View

def hello_view(request):
    # ip=request.META.get('HTTP_REFERER')
    return HttpResponse(f"hello, world")


def time_view(request):
    return HttpResponse(datetime.datetime.now().isoformat())


def index_view(request):
    return HttpResponse("<br>".join([reverse("h2"), reverse("t"), reverse("i")]))


def hello(request):
    name = request.GET.get("name")
    age = int(request.GET.get("age", 20))
    print(age)
    return HttpResponse(f'hello {name}')


def sum(request, a, b):
    result = 0
    return HttpResponse(f'Sum = {result}')
