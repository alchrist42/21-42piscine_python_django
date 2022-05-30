from django.views.generic.detail import DetailView
from ..models import Article

class Detail(DetailView):
    model = Article
    template_name = 'ex/detail.html'
