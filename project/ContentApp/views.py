from django.shortcuts import render

# Create your views here.
from models import Page
from django.http import HttpResponse , HttpResponseNotFound
from barrapunto import GetNews

news = ""

def UpDateNew (request) :
    global news
    news = GetNews()
    return = HttpResponse ('<br>Update News</br>')


def process(reques , recurso) :
    if request.method == "GET" :
        try :
            fila = Page.objects.get(name=recurso)
            return HttpResponse (fila.page + '<br><br>' + news)
        except Page.DoesNotExist:
            return HttpResponseNotFound ("Page Not Found")

    elif request.method == "PUT" :
        try :
            cuerpo = request.body
            fila = Page.objects.create(name = recurso,page = cuerpo)
            fila.save()
            return HttpResponse("Fila nueva creada")
        except :
            return HttpResponseNotFound ("Error")
