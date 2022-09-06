from django.urls import path
from .views import NewsList, NewsDetail, AuthorsList, AuthorDetail
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView

urlpatterns = [
    path('authors/', AuthorsList.as_view()),
    path('authors/<int:pk>', AuthorDetail.as_view()),
    path('news/', NewsList.as_view()),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name = 'sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name = 'sign/signup.html'),
         name='signup'),
    path('upgrade/', upgrade_me, name = 'upgrade')
]
