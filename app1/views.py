from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vistaUno(request):
    html="""
    <h1> hola mundo app1 </h1>
    """
    return HttpResponse(html)