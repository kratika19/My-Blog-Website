from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import View
from django.views.generic import ListView, DetailView


# Create your views here.


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         'posts': latest_posts
#     })

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = 'posts'


    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data



# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html",{
#         "all_posts" : all_posts,
#     })


class PostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    ordering = ["-date"]
    context_object_name = "all_posts"


# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug = slug)
#     return render(request, "blog/post-detail.html", {
#         'post' : identified_post,
#         'post_tags' : identified_post.tags.all()
#     })


class DetailPostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context