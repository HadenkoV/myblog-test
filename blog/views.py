from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from django.views import View
from django.urls import reverse
# Create your views here.

def index(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, "index.html", { "posts": latest_posts })


def posts(request):
    all_posts = Post.objects.all()
    return render(request, "all-posts.html", { "all_posts": all_posts })


class SinglePostView(View):
    template_name = "post-detail.html"
    model = Post
    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, self.template_name, context)
    
    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail", args=[slug]))
        
        
        context = {
            "post": post,
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        
        return render(request, self.template_name, context)

        