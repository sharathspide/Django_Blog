from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForms
#All of our blog post - ListView
#retrieve the single blog post -DetailView

# def home (request):
#     return render(request, 'Home.html',{})

class HomeView (ListView):
    model = Post
    template_name = 'Home.html'

class PostDetailView (DetailView):
    model = Post
    template_name = 'Post_Detail.html'

class CreatePostview (CreateView):
    model = Post
    form_class = PostForms
    template_name = 'AddPost.html'
    #fields = '__all__'
    #fields = ('title', 'body')