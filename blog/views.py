from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from.models import Post

def home_page_view(request):
    return render(request, "home.html")

def campaign_diary_view(request):
    posts = Post.objects.all()
    return render(request, "blog/campaign_diary.html", {'posts': posts})

def individual_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/individual_post.html", {'post':post})