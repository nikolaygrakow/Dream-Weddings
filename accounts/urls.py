from django.urls import path, include
from accounts.views import RegisterView, WeddingLoginView, WeddingLogoutView, ProfileDetailView, ProfileEditView, \
    WeddingPasswordChangeView

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
]