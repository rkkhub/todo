# Todo - API
    This is an RESTful API that has basic task manager features

## Schema Description
1. title (max length: 255) - Task title
2. completed (default value: False) - Tast status
3. section (max length: 128, default value: default) - Section to which a task belongs
4. date - Task created datetime - Date and time when the task was created

## Tech stack - initial setup
1. [Python](https://www.python.org/)
2. [Django](https://www.djangoproject.com/) - Web app framework for python
3. [Django Rest Framework](https://www.django-rest-framework.org/) - REST API framework for django
4. [Docker](https://www.docker.com/) -  Platform for developing, testing, and running applications

### Django commands
* Start a new django project
```
django-admin startproject todo
```
* Start a new app
```
python manage.py startapp todo
```
* Stage the model changes for database schema
```
python manage.py makemigrations
```
* Push the schema changes to the database
```
docker-compose run --rm app sh -c "python manage.py migrate"
```

### Docker commands
* Run server in local
```
docker-compose up
```
* Stops and removes containers
```
docker-compose down
```
* Run unit tests and linter check in local environment
```
docker-compose run --rm app sh -c "python manage.py test && flake8"
```
* Create super user
```
docker-compose run app sh -c "python manage.py createsuperuser"
```

### Dev notes:
super_user
user = dev_su@mytodo.com
pass = password
 
### Resources and References
[API Security](https://owasp.org/www-project-api-security/)
[Mark Down cheat sheet](https://www.markdownguide.org/cheat-sheet/)