from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import WeddingUserCreationForm


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    form_class = WeddingUserCreationForm
    success_url = reverse_lazy('accounts:login')
    success_message = "Your account has been created successfully!"

class WeddingLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "You have been logged in successfully!")
        return response


class WeddingLogoutView(LogoutView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        messages.success(request, "You have been logged out successfully!")
        return response