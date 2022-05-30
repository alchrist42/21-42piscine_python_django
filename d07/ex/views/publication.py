from django.views.generic import ListView
from django.views.generic.base import RedirectView
from ..models import Article, UserFavouriteArticle

class PublicationsView(ListView):
    model = Article
    template_name: str = 'ex/publications.html'
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)