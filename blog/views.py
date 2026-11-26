from django.shortcuts import render
from django.http import Http404

from .data import POSTS, CATEGORIES

def post_card_fragment(request, post_slug):
    post = next((post for post in POSTS if post["slug"] == post_slug and post["is_published"]), None)
    if post is None:
        raise Http404("Публикация не найдена")
    return render(request, "blog/post_card_body.html", {"post": post})


def post_list(request):
    q = request.GET.get("q", "").strip()
    cat = request.GET.get("cat", "").strip()

    posts = [post for post in POSTS if post["is_published"]]

    if cat:
        posts = [post for post in posts if post["category"]["name"] == cat]

    if q:
        posts = [post for post in posts if q.lower() in post["title"].lower()]    

    context = {
        "page_title": "Лента публикаций",
        "posts": posts,
        "categories": CATEGORIES,
        "q": q,
        "cat": cat,
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