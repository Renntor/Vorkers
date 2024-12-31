# WORKER MANAGEMENT API

Данный проект представляет собой микросервис для управления данными о работниках бригад. Он разработан на основе **Django** и **Django REST Framework**.

## УСТАНОВКА

### 1. Клонируйте репозиторий:
```
 git clone https://github.com/Renntor/Vorkers.git
```

### 2. Настройте .env файл

### 3. Установите зависимости:

```
pip install -r requirements.txt
```

### 4. Выполните миграции базы данных:

```
python manage.py migrate
```

### 5. Запустите сервер разработки:

```
python manage.py runserver
```

## Эндпоинты
1. Получение списка работников в бригаде
GET /api/v1/team/<team_id>/WorkerList

Возвращает список всех работников, принадлежащих указанной бригаде.

Пример ответа:
```
[
    {
        "id": 1,
        "full_name": "Иванов",
        "specialization": "Черновая отделка"
    },
    {
        "id": 3,
        "full_name": "Сидоров",
        "specialization": "Бригадир"
    }
]
```

2. Получение данных о работнике
GET /api/v1/worker/<worker_id>

Возвращает полную информацию о конкретном работнике.

Пример ответа:
```
{
    "id": 4,
    "name": "Сергеев",
    "salary": 20000,
    "specialization": "Прораб",
    "brigade_number": [
      {
          "number": 1
      },
      {
          "number": 2
      }
    ]
}
```
