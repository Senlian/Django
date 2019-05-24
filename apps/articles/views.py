from django.shortcuts import render, HttpResponse
from django.contrib.auth import get_user_model, views as auth_views
from accounts.views import LoginRequiredPostMixin


# Create your views here.
class ArticleListTitleView(LoginRequiredPostMixin, auth_views.TemplateView):
    def get(self, request, *args, **kwargs):
        articles = request.user.articles.all()
        context = self.get_context_data(**kwargs)
        context.update({'articles': articles})
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        articles = request.user.articles.all()
        return render(request, 'articles/article_intro_list.html', {'articles': articles})
