from django.shortcuts import render

from .models import Post
# Create your views here.


def post_list_view(request):
    post_objects = Post.objects.all()
    context = {
        'post_objects' : post_objects
    }
    return render(request, "posts/index.html", context)


def main_view(request):
    return render(request, "index.html")

def log_in_view(request):
    return render(request, "log_in.html")