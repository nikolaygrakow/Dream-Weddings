from django.urls import path
from inquiries import views

app_name = 'inquiries'

urlpatterns = [
    path('create/<int:pk>/', views.WeddingInquiryCreateView.as_view(), name='create-inquiry'),
    path('my-inquiries/', views.WeddingInquiryListView.as_view(), name='my-inquiries')
]

