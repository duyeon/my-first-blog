from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def keyboard(request):

    return JsonResponse({
        "type": "buttons",
        "buttons": ["1","2","3"]
    })

def home(request):

    return JsonResponse({

    })
