from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user
from .models import BlogArticles


# Create your views here.

def blog_title(request):
    blogs = BlogArticles.objects.all()
    user = get_user(request)
    # print(user.is_authenticated)
    return render(request, 'blog/titles.html', {'blogs': blogs, 'user': user})


def blog_articles(request, article_id):
    article = get_object_or_404(BlogArticles, id=article_id)
    return render(request, 'blog/content.html', {'article': article})
