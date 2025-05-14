from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

def home_page_view(request):
    return render(request, "home.html")

def accounts_page_view(request):
    return render(request, "login.html")

class CampaignDiaryView(ListView):
    model = Post
    template_name = "campaign_diary.html"
    ordering = ['-date']

# def campaign_diary_view(request):
#     posts = Post.objects.all()
#     return render(request, "blog/campaign_diary.html", {'posts': posts})

class IndividualPostView(DetailView):
    model = Post
    template_name = "individual_post.html"

# def individual_post_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "blog/individual_post.html", {'post':post})

class UploadReportView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "session_report.html"
    fields = ['title', 'campaign', 'session', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'campaign', 'session', 'text']

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("Campaign Diary")