from django.shortcuts import render
from django.http import Http404

from .data import POSTS

def post_card_fragment(request, post_slug):
    post = next((post for post in POSTS if post["slug"] == post_slug and post["is_published"]), None)
    if post is None:
        raise Http404("Публикация не найдена")
    return render(request, "blog/post_card_body.html", {"post": post})


def post_list(request):
    published = [post for post in POSTS if post["is_published"]]
    context = {
        "page_title": "Лента публикаций",
        "posts": published,
    }
    return render(request, "blog/post_list.html", context)


def about(request):
    context = {
        "page_title": "Обо мне",
    }
    return render(request, "blog/about.html", context)


def post_detail(request, post_slug):
    post = next((p for p in POSTS if p["slug"] == post_slug and p["is_published"]), None)
    
    if post is None:
        raise Http404("Публикация не найдена")
        
    context = {
        "post": post,
        "page_title": post["title"],
    }
    return render(request, "blog/post_detail.html", context)