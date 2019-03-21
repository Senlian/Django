from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .models import ArticleColumn, ArticlePost, ArticleComments, ArticleTag
from .forms import ArticleColumnForm, ArticlePostForm, ArticleCommentsForm, ArticleTagForm
import markdown
import json


# Create your views here.

@login_required(login_url=reverse_lazy('account:user_login'))
@method_decorator(csrf_exempt, name='POST')
def article_column(request):
    if request.method == "GET":
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()
        return render(request, 'article/column/article_column.html', {'columns': columns, 'column_form': column_form})
    if request.method == "POST":
        column_name = request.POST.get('column', '')
        columns = ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)
        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse('1')


@login_required(login_url=reverse_lazy('account:user_login'))
@require_POST
@method_decorator(csrf_exempt, name='POST')
def rename_article_column(request):
    column_name = request.POST.get('column_name', '')
    column_id = request.POST.get('column_id', '')

    try:
        column = ArticleColumn.objects.get(id=column_id)
        column.column = column_name
        column.save()
        return HttpResponse("1")
    except Exception as e:
        # raise e
        return HttpResponse("0")


@login_required(login_url=reverse_lazy('account:user_login'))
@require_POST
@method_decorator(csrf_exempt, name='POST')
def del_article_column(request):
    column_id = request.POST.get('column_id', '')
    try:
        column = ArticleColumn.objects.get(id=column_id)
        column.delete()
        return HttpResponse("1")
    except Exception as e:
        # raise e
        return HttpResponse("0")


@login_required(login_url=reverse_lazy('account:user_login'))
@method_decorator(csrf_exempt, name='POST')
def article_post(request):
    if request.method == 'POST':
        article_post_form = ArticlePostForm(request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.column = request.user.article_column.get(id=request.POST['column_id'])

                new_article.save()
                for tag in json.loads(request.POST.get('tags', [])):
                    mytag = request.user.tag.get(tag=tag)
                    new_article.article_tag.add(mytag)

                return HttpResponse('1')
            except Exception as e:

                return HttpResponse('2')
        else:
            return HttpResponse('3')

    article_post_form = ArticlePostForm()
    article_columns = request.user.article_column.all()
    article_tags = request.user.tag.all()
    return render(request, 'article/column/article_post.html',
                  {'article_post_form': article_post_form, 'article_columns': article_columns,
                   'article_tags': article_tags})


@login_required(login_url=reverse_lazy('account:user_login'))
@method_decorator(csrf_exempt, name='POST')
def article_list(request):
    articles = ArticlePost.objects.filter(author=request.user)
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    try:
        curpage = paginator.page(page)
        articles = curpage.object_list
    except PageNotAnInteger:
        curpage = paginator.page(1)
        articles = curpage.object_list
    except EmptyPage:
        curpage = paginator.page(paginator.num_pages)
        articles = curpage.object_list
    return render(request, 'article/article_list.html', {'articles': articles, 'page': curpage})


def article_detail(request, id, slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    import markdown
    body = markdown.markdown(article.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    article_comments = ArticleComments.objects.filter(article_id=id)

    import redis
    from django.conf import settings
    redis_cli = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)

    # 对集合中的article.id元素的值按照设定步长1增长，步长为负则减少
    redis_cli.zincrby('article_ranking', 1, article.id)
    # redis_cli.sadd('article_rankings:{0}'.format(article.id), request.user.username)
    total_views = redis_cli.incr('article:{0}:views'.format(article.id))

    article_ranking_ids = [int(id) for id in redis_cli.zrange('article_ranking', 0, -1, desc=True)[:10]]
    most_view_articles = list(ArticlePost.objects.filter(id__in=article_ranking_ids))
    most_view_articles.sort(key=lambda x: article_ranking_ids.index(x.id))
    if request.method == 'POST':
        article_comments_from = ArticleCommentsForm(request.POST)
        if article_comments_from.is_valid():
            new_comment = article_comments_from.save(commit=False)
            new_comment.author = request.user
            new_comment.article = article
            new_comment.save()
            # 重定向到当前页防止重复提交表单
            return HttpResponseRedirect(reverse_lazy('article:article_detail', kwargs={'id': id, 'slug': slug}))

    article_comments_from = ArticleCommentsForm()
    # 获取id列组成的列表，flat申明返回格式是list，否则是元组格式
    # values 获取到的值是字典形式
    article_tag_ids = article.article_tag.values_list('id', flat=True)
    similar_articles = ArticlePost.objects.filter(article_tag__in=article_tag_ids).exclude(id=article.id)
    similar_articles = similar_articles.annotate(tags=Count('article_tag')).order_by('-tags', '-created')


    return render(request, 'article/article.detail.html',
                  {'article': article, 'body': body, 'total_views': total_views, 'similar_articles': similar_articles,
                   'most_view_articles': most_view_articles, 'article_comments': article_comments,
                   'article_comments_from': article_comments_from})


@login_required(login_url=reverse_lazy('account:user_login'))
@method_decorator(csrf_exempt, name='POST')
def article_edit(request, article_id):
    if request.method == 'GET':
        article_columns = request.user.article_column.all()
        article = ArticlePost.objects.get(id=article_id)
        this_article_form = ArticlePostForm(initial={'title': article.title, 'body': article.body})
        this_article_column = article.column
        article_tags = ArticleTag.objects.all()
        has_tags = article.article_tag.all()

        return render(request, 'article/column/article_edit.html', {"article": article,
                                                                    "article_columns": article_columns,
                                                                    "this_article_form": this_article_form,
                                                                    "has_tags": has_tags,
                                                                    "article_tags": article_tags,
                                                                    "this_article_column": this_article_column})
    else:
        try:
            article = ArticlePost.objects.get(id=article_id)
            article.title = request.POST.get('title')
            article.column = request.user.article_column.get(id=request.POST.get('column_id'))

            article.body = request.POST.get('body')
            article.save()
            tags = json.loads(request.POST.get('tags', []))

            article.article_tag.clear()
            for tag in tags:
                mytag = request.user.tag.get(tag=tag)
                article.article_tag.add(mytag)
            return HttpResponse('1')
        except Exception as e:
            # print(ArticlePostForm(request.POST))
            print(request.POST)
            print(e)
            return HttpResponse('2')


@login_required(login_url=reverse_lazy('account:user_login'))
@require_POST
@method_decorator(csrf_exempt, name='POST')
def article_del(request):
    if request.method == 'POST':
        article_id = request.POST.get('article_id', '')
        try:
            article = ArticlePost.objects.get(id=article_id)
            article.delete()
            return HttpResponse('1')
        except Exception as e:
            return HttpResponse('2')


@login_required(login_url=reverse_lazy('account:user_login'))
@method_decorator(csrf_exempt, name='POST')
def article_tag(request):
    if request.method == 'GET':
        article_tag_form = ArticleTagForm()
        article_tags = ArticleTag.objects.filter(author=request.user)
        return render(request, 'article/article_tag.html',
                      {'article_tags': article_tags, 'article_tag_form': article_tag_form})

    article_tag_form = ArticleTagForm(request.POST)
    if article_tag_form.is_valid():
        try:
            new_tag = article_tag_form.save(commit=False)
            new_tag.author = request.user
            new_tag.save()
            return HttpResponse('1')
        except:
            return HttpResponse('2')
    else:
        return HttpResponse('3')


@login_required(login_url=reverse_lazy('account:user_login'))
@method_decorator(csrf_exempt, name='POST')
def rename_tag(request):
    tag_name = request.POST.get('tag', '')
    tag_id = request.POST.get('tag_id', '')
    try:
        new_Tag = ArticleTag.objects.get(id=tag_id)
        new_Tag.tag = tag_name
        new_Tag.save()
        return HttpResponse("1")
    except Exception as e:
        return HttpResponse("0")


@login_required(login_url=reverse_lazy('account:user_login'))
@method_decorator(csrf_exempt, name='POST')
def del_tag(request, tag_id):
    try:
        tag = ArticleTag.objects.get(id=tag_id)
        tag.delete()
        return HttpResponseRedirect(reverse_lazy('article:article_tag'))
    except Exception as e:
        print(e)
        return HttpResponseRedirect(reverse_lazy('article:article_tag'))
