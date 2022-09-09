from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Category, Post, PostCategory, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.shortcuts import get_object_or_404
from .models import *
from .filters import PostFilter
from .forms import PostForm
from .models import Post
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


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

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

class BaseRegisterView(CreateView):
    model = User
    from_class = BaseRegisterForm
    success_url = '/'

@ login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.fillter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')

