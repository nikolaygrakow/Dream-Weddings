from django.urls import path, include
from weddings import views

app_name = 'weddings'
urlpatterns = [
    path('', views.WeddingListView.as_view(), name='list'),
    path('create/', views.WeddingCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('', views.WeddingDetailsView.as_view(), name='details'),
        path('edit/', views.WeddingEditView.as_view(), name='edit'),
        path('delete/', views.WeddingDeleteView.as_view(), name='delete'),
        path('reviews/create/', views.ReviewCreateView.as_view(), name='review-create')
    ]))
]