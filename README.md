# api_yamdb
api_yamdb
Проект YaMDb - сервис отзывов на произведения

Тут пока ридми от старого проекта, нужно переписать



## Как запустить проект
Эти инструкции помогут вам запустить копию проекта на вашем компьютере.

### Клонирование репозитория
В терминале выбранной IDE: клонируйте репозиторий и перейдите в него.
```
git@github.com:nrthbnd/api_final_yatube.git
```
```
cd api_final_yatube
```

### Создание и активация виртуального окружения
Создание:
```
python -m venv venv
```
Активация:
```
source venv/Scripts/activate
```

### Установка зависимостей
Необходимо установить актуальные зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

### Выполнение миграций
```
python manage.py migrate
```

### Запуск проекта
```
python manage.py runserver
```

## Запуск тестов
Чтобы запустить тесты, необходимо в терминале запустить pytest:
```
pytest
```

## Доступные эндпоинты

-   `api/v1/posts/` : получение списка всех публикаций или создание новой. При указании параметров limit и offset выдача работает с пагинацией, анонимные запросы на создание публикации запрещены;
-   `api/v1/posts/{post_id}/` : получение, редактирование или удаление публикации по id. Получение публикации доступно всем пользователям, остальные функции - только для авторизованных пользователей;
-   `api/v1/posts/{post_id}/comments/` : получение списка всех комментариев к публикации с id=post_id или создание новой, при указании id публикации, которую хотим прокомментировать;
- `api/v1/posts/{post_id}/comments/{comment_id}/` : получение, редактирование или удаление комментариев по id у публикации с id=post_id;
-   `api/v1/groups/` : получение списка всех групп;
-   `api/v1/groups/{group_id}/` : получение информации о группе по id;
-   `api/v1/follow/` : получение всех подписок пользователя, сделавшего запрос, или подписка на пользователя, переданного в теле запроса. Анонимные запросы запрещены;
-   `api/v1/jwt/create/` : получение JWT-токена
-   `api/v1/jwt/refresh/` : обновление JWT-токена
-   `api/v1/jwt/verify/` : проверка JWT-токена

## Технологии

* Python 3.11.2
* Django 3.2.16
* Djangorestframework 3.12.4
* Djangorestframework-simplejwt 4.7.2 для работы с JWT токеном

## Примеры запросов

Пример POST-запроса с токеном авторизованного пользователя для добавления нового поста.
- POST .../api/v1/posts/
```
{
   "text": "Текст публикации",
   "image": "Изображение публикации",
   "group": 1
}
```
Пример ответа:
```
{
   "id": 1,
   "author": "Авторизованный пользователь 1",
   "text": "Текст публикации",
   "pub_date": "2019-08-24T14:15:22Z",
   "image": "Изображение публикации",
   "group": 1
}
```


Пример POST-запроса с токеном авторизованного пользователя для отправки нового комментария к посту с id=5.
- POST .../api/v1/posts/5/comments/
```
{
   "text": "Это пример комментария" 
}
```
Пример ответа:
```
{
   "id": 1,
   "author": "Авторизованный пользователь 1",
   "text": "Это пример комментария",
   "created": "2019-08-24T14:15:22Z",
   "post": 5
}
```

Пример POST-запроса с токеном авториованного пользователя для подписки на другого пользователя.
- POST .../api/v1/follow/
```
{
   "following": "Пользователь 2"
}
```
Пример ответа:
```
{
   "user": "Авторизованный пользователь 1",  
   "following": "Пользователь 2"
}
```

## Authors

 **Анастасия Боль** - [GitHub](https://github.com/nrthbnd)

