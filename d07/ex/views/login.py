from django.contrib.auth.views import LoginView

class Login(LoginView):
    template_name = "ex/login.html"
    next_page = 'ex:articles'

