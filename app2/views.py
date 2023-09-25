from django.shortcuts import render
from django.http import HttpResponse 

def vistaDos(request):
    html="""
    <h1> hola mundo app2 </h1>
    """
    return HttpResponse(html)