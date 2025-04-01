from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from.models import Post

def home_page_view(request):
    return render(request, "home.html")

def accounts_page_view(request):
    return render(request, "login.html")

class CampaignDiaryView(ListView):
    model = Post
    template_name = "campaign_diary.html"

# def campaign_diary_view(request):
#     posts = Post.objects.all()
#     return render(request, "blog/campaign_diary.html", {'posts': posts})

class IndividualPostView(DetailView):
    model = Post
    template_name = "individual_post.html"

# def individual_post_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "blog/individual_post.html", {'post':post})

class UploadReportView(CreateView):
    model = Post
    template_name = "session_report.html"
    fields = ['title', 'author', 'campaign', 'session', 'system', 'text']

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'campaign', 'session', 'system', 'text']