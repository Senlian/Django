from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth import views as auth_views
from common.gen_verify import draw_img

# Create your views here.

def DrawVerifyView(request):
    request.session['verify'] = draw_img()

    return JsonResponse({'refresh': 'ok'})

class IndexView(auth_views.TemplateView):
    template_name = 'blog/index.html'
    extra_context = {'title': 'SCSDN', 'site_title': '专业IT技术社区'}
