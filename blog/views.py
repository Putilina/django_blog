from django.shortcuts import render

from .data import POSTS


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


