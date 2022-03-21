# Todo - API

### Resources
[API Security](https://owasp.org/www-project-api-security/)



Start a new project
```
docker-compose run --rm app sh -c "django-admin startproject todo"
```

Start a new app
```
docker-compose run --rm app sh -c "python manage.py startapp todo"
```

To stage the model changes for database
```
docker-compose run --rm app sh -c "python manage.py makemigrations"
```

push the changes to the database
```
docker-compose run --rm app sh -c "python manage.py migrate"
```

Run server in local
```
docker-compose run --rm app sh -c "python manage.py runserver 0:8800"
```

For testing the setup
```
docker-compose run --rm app sh -c "python manage.py test && flake8"
```

To create super user
```
docker-compose run -it app sh -c "python manage.py createsuperuser"
```

Dev notes:
super_user
user = dev_su@mytodo.com
pass = password


user = dev_u@mytodo.com
pass = 
<!-- To do API -->

# models

- Tasks : task (varchar), date created (datetime), due date (date time), user(u_id), completed (bool), sectin (varchar)


# Add a new task