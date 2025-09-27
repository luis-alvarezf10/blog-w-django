from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "post_list"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = ["title", "body", "author"]

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ["title", "body"]
