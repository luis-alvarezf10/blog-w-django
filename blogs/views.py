<<<<<<< HEAD
=======
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
>>>>>>> feature/update
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "post_list"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
<<<<<<< HEAD
    
class PostCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "body", "author"]
    
=======

class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = ["title", "body", "author"]

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ["title", "body"]
>>>>>>> feature/update
