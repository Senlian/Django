from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth import views as auth_views
from common.gen_verify import draw_img
from common.utils.paginator import paginator

from articles.models import Articles


# Create your views here.

def DrawVerifyView(request):
    request.session['verify'] = draw_img()
    return JsonResponse({'refresh': 'ok'})


class IndexView(auth_views.TemplateView):
    template_name = 'blog/index.html'
    extra_context = {'title': 'SCSDN', 'site_title': '专业IT技术社区'}

    def get(self, request, *args, **kwargs):
        articles = Articles.objects.all().order_by('-update')
        self.extra_context.update(paginator(request, articles))
        return super().get(request, *args, **kwargs)
