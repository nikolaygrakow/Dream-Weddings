from django.urls import path, include
from services import views

app_name = 'services'
urlpatterns = [
    path('', views.ServiceCategoriesView.as_view(), name='list'),
    path('category/<str:category>/', views.ServiceByCategoryView.as_view(), name='category'),
    path('create/', views.ServiceCreateView.as_view(), name='create'),
    path('<int:pk>/', include([
        path('', views.ServiceDetailsView.as_view(), name='details'),
        path('edit/', views.ServiceEditView.as_view(), name='edit'),
        path('delete/', views.ServiceDeleteView.as_view(), name='delete')
    ]))
]