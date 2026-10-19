# Lab 07 — JavaScript

На странице архива:

1. `helloworld.js` — вывод студентов в Console и фильтры (группа / средний балл).
2. `fold-post.js` — сворачивание карточки через класс `folded` на `.one-post`.

## Дерево

```
lab07
├── manage.py
├── blog/
└── articles/
    └── static/
        ├── css/article.css
        └── js/
            ├── helloworld.js
            └── fold-post.js
```

## Запуск

```bash
cd lab07
python3 manage.py migrate
python3 manage.py runserver
```

Откройте http://127.0.0.1:8000/ и панель разработчика (Console / Elements).
