from django.urls import path
from .views import NewsList, NewsDetail, AuthorsList, AuthorDetail

path('authors/', AuthorsList.as_view()),
path('authors/<int:pk>', AuthorDetail.as_view()),
path('news/', NewsList.as_view()),
path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),