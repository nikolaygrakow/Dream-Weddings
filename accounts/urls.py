from django.urls import path, include
from accounts.views import RegisterView, WeddingLoginView, WeddingLogoutView, ProfileDetailView, ProfileEditView, \
    WeddingPasswordChangeView, WeddingPasswordResetView, WeddingPasswordResetDoneView, WeddingPasswordResetConfirmView, \
    WeddingPasswordResetCompleteView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', WeddingLoginView.as_view(), name='login'),
    path('logout/', WeddingLogoutView.as_view(), name='logout'),
    path('profile/', include([
        path('details/', ProfileDetailView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('change-password/', WeddingPasswordChangeView.as_view(), name='change-password'),
    ])),
    path('reset-password/', include([
        path('', WeddingPasswordResetView.as_view(), name='reset-password'),
        path('done/', WeddingPasswordResetDoneView.as_view(), name='reset-password-done'),
        path('confirm/<uidb64>/<token>/', WeddingPasswordResetConfirmView.as_view(), name='reset-password-confirm'),
        path('complete/', WeddingPasswordResetCompleteView.as_view(), name='reset-password-complete'),
    ])),
]