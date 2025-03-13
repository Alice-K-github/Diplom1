from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from users.forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('diary/home.html')


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'
    success_url = reverse_lazy('')


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
