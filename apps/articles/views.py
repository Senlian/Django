from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth import get_user_model, views as auth_views
from django.views import generic

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from accounts.views import LoginRequiredPostMixin
from articles.models import Articles
from common.utils.paginator import paginator

UserModel = get_user_model()


# Create your views here.
class ArticleBackListView(LoginRequiredPostMixin, auth_views.TemplateView):
    template_name = 'articles/back_stage_articles.html'
    extra_context = {"title": "博客管理", 'site_title': 'SCSDN博客'}

    def get(self, request, *args, **kwargs):
        articles = request.user.articles.all().order_by('-top')
        publics = articles.filter(status='1')
        privates = articles.filter(status='2')
        drafts = articles.filter(status='3')
        deleteds = articles.filter(status='4')
        self.extra_context.update(paginator(request, articles))
        self.extra_context.update({
            'total': articles.count,
            'publics': publics,
            'privates': privates,
            'drafts': drafts,
            'deleteds': deleteds,
        })
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        layid = request.POST.get('layid', '1')
        articles = request.user.articles.all().order_by('-top')
        response_context = {'layid': layid}
        if str(layid) != '0':
            articles = articles.filter(status=layid)
        response_context.update(paginator(request, articles))
        return render(request, 'articles/base/article_intro_list.html', response_context)


class ArticleListView(auth_views.TemplateView):
    template_name = 'articles/article_list_author.html'
    extra_context = {'site_title': 'SCSDN博客'}

    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        author = UserModel._default_manager.get(username=username)
        if username == request.user.username:
            articles = author.articles.all()
        else:
            articles = author.articles.filter(status='1')

        if articles:
            self.extra_context.update({
                'title': '{0}的博客'.format(username),
                'article': articles.first()})
        else:
            self.extra_context.update({
                'title': '{0}的博客'.format(username),
                'author': author})
        self.extra_context.update(paginator(request, articles))
        return super().get(request, *args, **kwargs)


class ArticleShowView(auth_views.TemplateView):
    template_name = 'articles/article_show.html'
    extra_context = {'site_title': 'SCSDN博客'}

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Articles, id=kwargs['id'], slug=kwargs['slug'])
        self.extra_context.update({"title": article.title, 'article': article})
        return super().get(request, *args, **kwargs)


class ArticleActionsView(generic.View):
    pass
