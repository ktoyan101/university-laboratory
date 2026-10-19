from django.http import Http404
from django.shortcuts import redirect, render


def archive(request):
    from .models import Article

    articles = Article.objects.all().order_by("-created_date")
    return render(request, "archive.html", {"articles": articles})


def get_article(request, article_id):
    from .models import Article

    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Запись не найдена")

    return render(request, "article.html", {"article": article})


def create_post(request):
    from .models import Article

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
            return render(request, "create_post.html", {"form": form})

        if Article.objects.filter(title=title).exists():
            form["errors"] = "Такое название уже занято"
            return render(request, "create_post.html", {"form": form})

        article = Article.objects.create(
            title=title,
            text=text,
            author=request.user
        )

        return redirect("get_article", article_id=article.id)

    return render(request, "create_post.html", {"form": {}})


def register(request):
    from django.contrib.auth.models import User

    if request.user.is_authenticated:
        return redirect("archive")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        password_confirm = request.POST.get("password_confirm", "")

        form = {
            "username": username,
            "email": email,
            "errors": "",
        }

        if not username or not email or not password or not password_confirm:
            form["errors"] = "Проверьте, что все поля заполнены"
            return render(request, "register.html", {"form": form})

        if password != password_confirm:
            form["errors"] = "Пароль и подтверждение различаются"
            return render(request, "register.html", {"form": form})

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect("user_login")
        else:
            form["errors"] = "Логин уже используется"
            return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": {}})


def user_login(request):
    from django.contrib.auth import authenticate, login

    if request.user.is_authenticated:
        return redirect("archive")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        form = {
            "username": username,
            "errors": "",
        }

        if not username or not password:
            form["errors"] = "Укажите логин и пароль"
            return render(request, "login.html", {"form": form})

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is None:
            form["errors"] = "Не удалось войти: проверьте данные"
            return render(request, "login.html", {"form": form})

        login(request, user)

        return redirect("archive")

    return render(request, "login.html", {"form": {}})


def user_logout(request):
    from django.contrib.auth import logout

    logout(request)
    return redirect("archive")
