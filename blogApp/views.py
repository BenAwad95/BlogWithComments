from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Post, Comment, CommentFormModel

# * import view generic
from django.views.generic import ListView

class PostView(ListView):
    model = Post

# class PostDetailView(DetailView):
#     model = Post

# class CreateCommentView(CreateView):
#     model = Comment


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentFormModel()
    if request.method == 'POST':
        author = request.POST.get('author')
        body = request.POST.get('body')
        Comment.objects.create(author=author, body=body, post=post, created_on=datetime.now())
    context = {
        'object':post,
        'form': form
    }
    return render(request, 'blogApp/post_detail.html', context=context)
