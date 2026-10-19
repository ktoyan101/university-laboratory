from django.http import Http404
from django.shortcuts import redirect, render

from .models import Article


def archive(request):
    return render(
        request,
        'archive.html',
        {'posts': Article.objects.all()}
    )


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(
            request,
            'article.html',
            {'post': post}
        )
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if request.user.is_anonymous:
        raise Http404

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        text = request.POST.get("text", "").strip()

        form = {
            "title": title,
            "text": text,
            "errors": "",
        }

        if not title or not text:
            form["errors"] = "Заполните все поля формы"
            return render(
                request,
                "create_post.html",
                {"form": form}
            )

        if Article.objects.filter(title=title).exists():
            form["errors"] = "Такое название уже занято"
            return render(
                request,
                "create_post.html",
                {"form": form}
            )

        article = Article.objects.create(
            title=title,
            text=text,
            author=request.user
        )

        return redirect(
            "get_article",
            article_id=article.id
        )

    return render(
        request,
        "create_post.html",
        {"form": {}}
    )
