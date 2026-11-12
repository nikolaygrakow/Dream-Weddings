from django.urls import path
from accounts.views import RegisterView, WeddingLoginView, WeddingLogoutView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', WeddingLoginView.as_view(), name='login'),
    path('logout/', WeddingLogoutView.as_view(), name='logout'),

]