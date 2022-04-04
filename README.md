# BlogApp

**Стек**
- Flask
- PostgreSQL
- SQLAlchemy

**Функционал**
- Возможность выкладывать посты,редактировать
- Админка с авторизацией администратора
- Редактировать и добавлять посты может 
только авторизованный пользователь
- Есть теги к каждому посту, по тегу можно
 смотреть список постов


Для запуска проекта необходимо:
Установить зависимости:

```bash
pip install -r requirements.txt
```

Для миграций в БД:

```bash
flask db migrate
flask db upgrade
```



![2022-04-04_15-28-23](https://user-images.githubusercontent.com/85485992/161543719-a2761d51-5b0e-41bb-8a95-502eec01b020.png)
![2022-04-04_15-26-08](https://user-images.githubusercontent.com/85485992/161544898-63a2a302-7afe-4cab-82bf-31e633f820c0.png)
![2022-04-04_15-25-37](https://user-images.githubusercontent.com/85485992/161543758-cf5570bd-9c3b-4d1b-9d4d-f040147232ef.png)

