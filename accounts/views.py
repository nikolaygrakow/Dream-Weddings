from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from accounts.utils import send_password_changed_email
from accounts.forms import WeddingUserCreationForm, WeddingUserEditForm


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    form_class = WeddingUserCreationForm
    success_url = reverse_lazy('accounts:login')
    success_message = "Your account has been created successfully!"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts:profile-details')
        return super().dispatch(request, *args, **kwargs)

class WeddingLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "You have been logged in successfully!")
        return response

class WeddingLogoutView(LogoutView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        messages.success(request, "You have been logged out successfully!")
        return response

class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile-details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user


class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = WeddingUserEditForm
    template_name = 'accounts/profile-edit.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('accounts:profile-details')


    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your profile has been updated successfully!")
        return response

class WeddingPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/password-change.html'
    success_url = reverse_lazy('accounts:profile-details')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_password_changed_email(self.request.user)
        messages.success(self.request, "Your password has been changed successfully!")
        return response


class WeddingPasswordResetView(PasswordResetView):
    template_name = 'accounts/password-reset.html'
    email_template_name = 'accounts/password-reset-email.html'
    success_url = reverse_lazy('accounts:reset-password-done')

class WeddingPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password-reset-done.html'

class WeddingPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password-reset-confirm.html'
    success_url = reverse_lazy('accounts:reset-password-complete')

    def form_valid(self, form):
        response = super().form_valid(form)
        send_password_changed_email(self.user)
        return response

class WeddingPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password-reset-complete.html'