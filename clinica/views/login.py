from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy



class LoginUsuarioView(LoginView):
    template_name = 'auth/login.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        return form

    def get_success_url(self):
        user = self.request.user

        if not hasattr(user, 'profissional'):
            return reverse_lazy('login')

        tipo = user.profissional.tipo.strip().lower()

        if tipo == 'medico':
            return reverse_lazy('medico-consultas')

        elif tipo == 'recepcionista':
            return reverse_lazy('consultas-lista')

        return reverse_lazy('login')

class LogoutUsuarioView(LogoutView):
    next_page = reverse_lazy('login')