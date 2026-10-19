# Lab 01 — Python и Django

## Дерево

```
lab01
├── README.md
├── helloworld.py
├── mygroup.py
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
```

В корне репозитория лежит `manage.py` для Django-проекта Lab 01.

## Скрипты

```bash
cd lab01
python3 helloworld.py
python3 mygroup.py
```

## Django

Из корня репозитория:

```bash
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

Админка: http://127.0.0.1:8000/admin/
