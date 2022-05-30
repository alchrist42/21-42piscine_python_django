from django.views.generic.edit import CreateView
from ..models import Article
from django.shortcuts import redirect


class Publish(CreateView):
    template_name = "ex/publish.html"
    model = Article
    success_url = '/'
    fields = ['title', 'synopsis', 'content']

    def form_valid(self, form):
        # Мы используем ModelForm, а его метод save() возвращает инстанс
        # модели, связанный с формой. Аргумент commit=False говорит о том, что
        # записывать модель в базу рановато.
        instance = form.save(commit=False)

        # Теперь, когда у нас есть несохранённая модель, можно ей чего-нибудь
        # накрутить. Например, заполнить внешний ключ на auth.User. У нас же
        # блог, а не анонимный имижборд, правда?
        instance.author = self.request.user
        instance.save() 

        return redirect('/')
    