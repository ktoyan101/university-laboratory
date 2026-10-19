# Lab 06 — auth

Страницы `/register/` и `/login/`, ссылки в шапке архива.

## Дерево

```
lab06
├── manage.py
├── blog/urls.py
└── articles/
    ├── views.py
    └── templates/
        ├── register.html
        └── login.html
```

## Запуск

```bash
cd lab06
python3 manage.py migrate
python3 manage.py runserver
```
