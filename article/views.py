from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.http import HttpResponse

from .models import ArticleColumn, ArticlePost
from .forms import ArticleColumnForm, ArticlePostForm


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
    print(column_name)
    print(column_id)
    try:
        column = ArticleColumn.objects.get(id=column_id)
        column.column = column_name
        column.save()
        return HttpResponse("1")
    except Exception as e:
        raise e
        # return HttpResponse("0")


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
                # new_article.column = ArticleColumn.objects.filter(user=request.user)
                new_article.save()
                return HttpResponse('1')
            except Exception as e:
                return HttpResponse('2')
        else:
            print(article_post_form.errors)
            return HttpResponse('3')
    article_post_form = ArticlePostForm()
    article_columns = request.user.article_column.all()
    return render(request, 'article/column/article_post.html',
                  {'article_post_form': article_post_form, 'article_columns': article_columns})
