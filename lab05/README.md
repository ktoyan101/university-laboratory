# Lab 05 — создание поста

Форма `/article/new/` с проверкой уникальности заголовка.

## Дерево

```
lab05
├── manage.py
├── blog/
└── articles/
    ├── views.py
    └── templates/create_post.html
```

## Запуск

```bash
cd lab05
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

Создание поста доступно только авторизованному пользователю.
