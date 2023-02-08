from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.ShowView.as_view(), name='home'),
    path('about', views.contacti, name='contacti'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    # отслеживание строки slug или str
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
    path('news/add', views.CreateNewsView.as_view(), name='news-add'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete'),
    path('user/<str:username>', views.UserAllNewsView.as_view(), name='user-news')
]