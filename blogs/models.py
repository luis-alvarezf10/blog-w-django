from django.db import models
<<<<<<< HEAD
from django.urls import reverse 
=======
from django.urls import reverse
>>>>>>> feature/update


# Create your models here :).
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
<<<<<<< HEAD

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
=======
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
>>>>>>> feature/update
