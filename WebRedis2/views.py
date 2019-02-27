from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from common.pyredis import client
import json


# Create your views here.


def index(request):
    return render(request, 'WebRedis/index.html')

# @csrf_exempt
def index_aside(request):
    return render(request=request, template_name="WebRedis/index-aside.html")
