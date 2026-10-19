# Lab 03 — модель Article

Блог: проект `blog`, приложение `articles`.

## Дерево

```
lab03
├── manage.py
├── blog/
└── articles/
    ├── models.py
    ├── admin.py
    ├── views.py
    └── templates/archive.html
```

## Запуск

```bash
cd lab03
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

Главная страница показывает архив статей.
