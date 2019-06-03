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


class MarkDownView(auth_views.TemplateView):
    config = {
        'width': '90%',
        'height': 500,
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                    "h1", "h2", "h3", "h4", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                    "emoji", "html-entities", "pagebreak", "|",
                    "goto-line", "watch", "preview", "fullscreen", "clear", "search", "|",
                    "help", "info"],
        'upload_image_formats': ["jpg", "JPG", "jpeg", "JPEG", "gif", "GIF", "png",
                                 "PNG", "bmp", "BMP", "webp", "WEBP"],
        'image_floder': 'editor',
        'theme': 'default',  # dark / default
        'preview_theme': 'default',  # dark / default
        'editor_theme': 'default',  # pastel-on-dark / default
        'toolbar_autofixed': True,
        'search_replace': True,
        'emoji': True,
        'tex': True,
        'flow_chart': True,
        'sequence': True,
        'language': 'zh'  # zh / en
    }

    extra_context = {'config': config,'title': 'MarkDown测试', 'site_title': 'SCSDN'}
    template_name = 'markdown/markdown_view.html'
