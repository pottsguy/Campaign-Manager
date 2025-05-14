from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Campaign
from django.db import models
from django.db.models import Q

def home_page_view(request):
    return render(request, "home.html")

def accounts_page_view(request):
    return render(request, "login.html")

class CampaignDiaryView(ListView):
    model = Post
    template_name = "campaign_diary.html"
    ordering = ['-date']

    # this part is recent - delete to reset to stable state START
    def get_queryset(self):
        queryset = super().get_queryset()
        campaign_id = self.request.GET.get('campaign')
        if campaign_id:
            queryset = queryset.filter(campaign__id=campaign_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campaigns'] = Campaign.objects.filter(
            Q(users=self.request.user) | Q(host=self.request.user)
        ).distinct()
        context['selected_campaign'] = self.request.GET.get('campaign', '')
        return context
    # this part is recent - delete to reset to stable state END

# def campaign_diary_view(request):
#     posts = Post.objects.all()
#     return render(request, "blog/campaign_diary.html", {'posts': posts})

class IndividualPostView(DetailView):
    model = Post
    template_name = "individual_post.html"

# def individual_post_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "blog/individual_post.html", {'post':post})

# class UploadReportView(LoginRequiredMixin,CreateView):
#     model = Post
#     template_name = "session_report.html"
#     fields = ['title', 'campaign', 'session', 'text']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

class UploadReportView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "session_report.html"
    fields = ['title', 'campaign', 'session', 'text']

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Only show campaigns where the user is a participant or the host
        from blog.models import Campaign  # or adjust import as needed
        from django.db import models
        form.fields['campaign'].queryset = Campaign.objects.filter(
            models.Q(users=self.request.user) | models.Q(host=self.request.user)
        ).distinct()
        return form

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