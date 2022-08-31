from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import get_object_or_404
from .models import *
from .filters import PostFilter
from .forms import PostForm
from .models import Post

class AuthorList(ListView):
    model = Author
    context_object_name = 'Authors'
    template_name = 'news/author_list.html'

class Post(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'Post'

class PostCategory(CreateView):
    model = Post
    fields = ['__all__']

class ProductCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.quantity = 13
        return super().form_valid(form)