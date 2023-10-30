from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
#All of our blog post - ListView
#retrieve the single blog post -DetailView

# def home (request):
#     return render(request, 'Home.html',{})

class HomeView (ListView):
    model = Post
    template_name = 'Home.html'

class PostDetail (DetailView):
    model = Post
    template_name = 'Post_Detail.html'