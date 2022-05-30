from django.views.generic import ListView
from django.views.generic.base import RedirectView
from ..models import UserFavouriteArticle


class FavoriteView(ListView):
    model = UserFavouriteArticle
    template_name: str = "ex/favorites.html"

    # def get_queryset(self):
    #     gs = Article.objects.filter(favorites__contains=self.request.user)
