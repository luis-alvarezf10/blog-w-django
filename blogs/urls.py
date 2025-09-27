from django.urls import path
<<<<<<< HEAD
from .views import PostListView, PostDetailView, PostCreateView
=======
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView
>>>>>>> feature/update

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),
<<<<<<< HEAD
=======
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
>>>>>>> feature/update
]
