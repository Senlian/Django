from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth import get_user_model, views as auth_views
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from accounts.views import LoginRequiredPostMixin
from articles.models import Articles


# Create your views here.
class ArticleListTitleView(LoginRequiredPostMixin, auth_views.TemplateView):
    template_name = 'articles/back_stage.html'
    extra_context = {"title": "博客管理", 'site_title': 'SCSDN博客'}

    def get(self, request, *args, **kwargs):
        articles = request.user.articles.all().order_by('-top')
        publics = articles.filter(status=1)
        privates = articles.filter(status=2)
        drafts = articles.filter(status=3)
        deleteds = articles.filter(status=3)

        context = self.get_context_data(**kwargs)
        context.update({
            'articles': articles,
            'publics': publics,
            'privates': privates,
            'drafts': drafts,
            'deleteds': deleteds,
        })
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        layid = request.POST.get('layid', '1')
        articles = request.user.articles.all().order_by('-top')
        if str(layid) != '0':
            articles = articles.filter(status=layid)
        return render(request, 'articles/article_intro_list.html', {'articles': articles, 'layid': layid})


class ArticleShowView(auth_views.TemplateView):
    template_name = 'articles/article_show.html'
    extra_context = {'site_title': 'SCSDN博客'}

    def get(self, request, *args, **kwargs):
        article = (get_object_or_404(Articles, id=kwargs['id'], slug=kwargs['slug']))
        self.extra_context.update({"title": article.title, 'article': article})
        return super().get(request, *args, **kwargs)
