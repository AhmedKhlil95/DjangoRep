from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField(("Enter You post here!"))

    


    # def __str__(self):
        # return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
#     author = models.CharField(max_length=100)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'

# models.py

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    
