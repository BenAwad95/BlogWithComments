from django.db import models
from django.db.models import fields
from django.urls import reverse
from django.forms import ModelForm
class Category(models.Model):
    name = models.CharField(verbose_name='gategory', max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(verbose_name='title' , max_length=50)
    body = models.TextField(verbose_name='body')
    created_on = models.DateTimeField(verbose_name='created on' , auto_now_add=True)
    last_modified = models.DateTimeField(verbose_name='last modified' , auto_now=True)
    categories = models.ManyToManyField(Category, verbose_name=("categories"), related_name='posts')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blogApp:post_detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    author = models.CharField(verbose_name=("author"), max_length=20)
    body = models.TextField(verbose_name=("comment body"))
    created_on = models.DateTimeField(verbose_name=("created on"), auto_now_add=True)
    post = models.ForeignKey(Post, verbose_name=("post"), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post} post: comment by {self.author}"
    
    def get_absolute_url(self):
        return reverse("blogApp:post_detail", kwargs={"pk": self.pk})

class CommentFormModel(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']