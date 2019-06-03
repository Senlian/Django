from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import get_user_model, views as auth_views
from django.views import generic

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db.models import Q

from accounts.views import LoginRequiredPostMixin
from articles.models import Articles
from common.utils.paginator import paginator

from articles.forms import ArticleSearchForm

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
            articles = articles.filter(status=layid).order_by('-top')
        response_context.update(paginator(request, articles))
        return render(request, 'articles/base/article_intro_list.html', response_context)


class ArticleListView(auth_views.TemplateView):
    template_name = 'articles/article_list_author.html'
    extra_context = {'site_title': 'SCSDN博客'}

    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        author = UserModel._default_manager.get(username=username)
        if username == request.user.username:
            articles = author.articles.all().order_by('-top')
        else:
            articles = author.articles.filter(status='1').order_by('-top')

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
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        method = request.POST.get('method', '')
        article_id = request.POST.get('option', '')
        if not (method and article_id):
            return JsonResponse({'status': 'not ok'})
        article = Articles.objects.get(id=int(article_id))
        if method.lower() == 'settop':
            article.set_top()
        elif method.lower() == 'setallowreply':
            article.set_allowreply()
        elif method.lower() == 'delete':
            article.delete()
        elif method.lower() == 'focus':
            article.author.set_fans(request.user)
        elif method.lower() == 'unfollow':
            request.user.set_unfollow(article.author)
        else:
            return JsonResponse({'status': 'not ok'})

        return JsonResponse({'status': 'ok'})


class ArticleSearchView(auth_views.TemplateView):
    template_name = 'blog/index.html'
    extra_context = {'title': 'SCSDN', 'site_title': '专业IT技术社区'}

    def post(self, request, *args, **kwargs):
        search = request.POST.get('search')
        self.extra_context.update({'title': search, 'site_title': 'SCSDN搜索'})
        form = ArticleSearchForm(request.POST)
        articles = {} if not form.is_valid() else form.cleaned_data['search']
        self.extra_context.update(paginator(request, articles))
        return super().get(request, *args, **kwargs)
