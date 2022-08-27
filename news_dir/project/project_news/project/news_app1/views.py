from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import get_object_or_404
from .models import *

class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/author_list.html'

class Post(DetailView):
    model = Post
    context_object_name = 'Post'

class PostCategory(CreateView):
    model = Post
    fields = ['__all__']