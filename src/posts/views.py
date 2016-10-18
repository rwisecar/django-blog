from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_create(request):
    return HttpResponse("<h1>Hello</h1>")

def post_detail(request):
    instance = get_object_or_404(Post, title="Test Post")
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "list"
    }
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My User List"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }

    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h1>Try This:</h1>")

def post_delete(request):
    return HttpResponse("<h1>Exterminate</h1>")
