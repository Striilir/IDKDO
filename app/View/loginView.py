from django.views.generic import FormView

from app.Forms.loginForm import LoginForm


class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
