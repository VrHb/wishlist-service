# Сервис для ведения списков желаний

Сервис позволяет быстро делиться желаниями в основных месенджерах.

-   Основное преимущество - быстрота

![Скрин главной страницы](images/main.jpg)

## Установка проекта

### Переменные окружения

-   Создаем .env файл

```shell
touch ./wishlists/.env
```

-   Секретный ключ для проекта django, [django secret key](https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-SECRET_KEY)

```shell
echo 'DJANGO_SECRET_KEY=<ваш ключ>' >> ./wishlists/.env
```

-   Настройка debug, для разработки установите

```shell
echo 'DEBUG=1' >> ./wishlists/.env
```

-   Директория для сохранения статики при деплое проекта и выполнении `collectstatis`

```shell
echo 'STATIC_DIR_NAME=<название>' >> ./withlists/.env
```

-   Переменные окружения для использования `social-auth-app-django`

-   Url конфиг для postgresql, [как настроить](https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes)

```shell
echo 'PSQL_URL=<url базы данных>' >> ./wishlists/.env
```

### Запуск

1. выполните миграции в бд

```shell
python manage.py migrate
```

2. Создайте администратора

```shell
python manage.py createsuperuser
```

3. Запусстите сервер

```shell
python manage.py runserver
```

#### Парсер цитат

Сайт генерирует цитаты на странице со списками, можно распарсить их

- Использование:

```sh 
python quotes_parser.py --help
```

- Пример:

```sh 
python quotes_parser.py --start_page 1 --end_page 5 --json_path ./quotes
```
