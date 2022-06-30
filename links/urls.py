from . import views
from django.urls import path

app_name = 'links'

urlpatterns = [
    path('', views.PostListAPI.as_view(), name= 'api_list'),
    path('create/', views.PostCreateAPI.as_view(), name= 'api_create'),
    path('update/<int:pk>', views.PostUpdateAPI.as_view(), name= 'api_update'),
    path('delete/<int:pk>', views.PostDeleteAPI.as_view(), name= 'api_delete'),
]