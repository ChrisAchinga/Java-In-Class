from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# def home(request):
#     return render(request, 'home.html', {})

class homeView(ListView):
    model = Post
    template_name = 'home.html'

class detailView(DetailView):
    model = Post
    template_name = 'article_details.html'