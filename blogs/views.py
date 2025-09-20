from django.views.generic import ListView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'post_list'
    

