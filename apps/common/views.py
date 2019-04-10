from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from common.gen_verify import draw_img

# Create your views here.
def CreateVerifyView(request):
    request.session['verify'] = draw_img()
    return JsonResponse({'refresh': 'ok'})
