from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.urls import reverse_lazy
from blog.models import Post
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView



class PostListView(generic.ListView):
   model = Post

class PostCreateView(generic.CreateView):
   model = Post
   fields = '__all__'
   success_url  = reverse_lazy('blog:all')

class PostDetailView(generic.DetailView):
    model = Post

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = '__all__'
    success_url  = reverse_lazy('blog:all')

class PostDeleteView(generic.DeleteView):
    model = Post

    fields = '__all__'
    success_url  = reverse_lazy('blog:all')
    
