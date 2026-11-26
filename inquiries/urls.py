from django.urls import path, include
from inquiries import views

app_name = 'inquiries'

urlpatterns = [
    path('create/<int:pk>/', views.WeddingInquiryCreateView.as_view(), name='create-inquiry'),
    path('my-inquiries/', views.WeddingInquiryListView.as_view(), name='my-inquiries'),
    path('inquiry/<int:pk>/', views.WeddingInquiryDetailView.as_view(), name='inquiry-details'),
    path('management/', include([
        path('', views.WeddingInquiryManagementListView.as_view(), name='management'),
        path('<int:pk>/', include([
            path('', views.WeddingInquiryManagementDetailView.as_view(), name='management-details'),
            path('update-status/', views.WeddingInquiryStatusUpdateView.as_view(), name='update-status')
        ]))
    ])),
]

