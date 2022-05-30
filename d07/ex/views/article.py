from django.views.generic import ListView
from django.views.generic.base import RedirectView
from ..models import Article, UserFavouriteArticle

class IndexRedirect(RedirectView):
    url = "articles"

class ArticlesView(ListView):
    template_name = 'ex/articles.html'
    model = Article


