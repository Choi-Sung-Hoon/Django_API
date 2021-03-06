Django_API [![Build Status](https://travis-ci.com/Choi-Sung-Hoon/Django_API.svg?branch=master)](https://travis-ci.com/Choi-Sung-Hoon/Django_API) [![Coverage Status](https://coveralls.io/repos/github/Choi-Sung-Hoon/Django_API/badge.svg?branch=master)](https://coveralls.io/github/Choi-Sung-Hoon/Django_API?branch=master)
==========

REST API project for a basic poll application applied CI and TDD. This project is managed by Travis CI.

README: [한국어](README.ko.md), [English](README.md)  

<br>

Project Goal
----------

1. Learn **how to design REST API in Python**  
2. Learn **how to make good test**  
3. Learn **how CI/CD works**  
4. Understand Django structure  

<br>

Endpoints
----------

- `/polls/`
- `/polls/<pk>/`
- `/polls/<pk>/choices/`
- `/polls/<pk>/choices/<choice_pk>/`
- `/polls/<pk>/choices/<choice_pk/vote/`
- `/login/`

<br>

Prerequisites
----------

- [virtualenv](https://pypi.org/project/virtualenv/)

<br>

Installation
----------

1. Clone this repository
    ```
    $ git clone git@github.com:Choi-Sung-Hoon/Django_API.git
    ```
    
2. Move to the cloned repository
    ```
    $ cd Django_API
    ```
    
3. Create a virtual environment
    ```
    $ virtualenv django
    Using base prefix '/usr'
    New python executable in /home/ubuntu/Django_API/django/bin/python3.6
    Also creating executable in /home/ubuntu/Django_API/django/bin/python
    Installing setuptools, pip, wheel...
    done.
    ```
    
4. Activate the virtual environment
    ```
    $ source django/bin/activate
    ```
    
5. Install pip packages required
    ```
    (django)$ pip install -r requirements.txt
    ```
    
6. Move to Django project directory
    ```
    (django)$ cd pollsapi
    ```
    
7. Build database for the project
    ```
    (django)$ python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, authtoken, contenttypes, polls, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying admin.0003_logentry_add_action_flag_choices... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying auth.0009_alter_user_last_name_max_length... OK
      Applying auth.0010_alter_group_name_max_length... OK
      Applying auth.0011_update_proxy_permissions... OK
      Applying authtoken.0001_initial... OK
      Applying authtoken.0002_auto_20160226_1747... OK
      Applying polls.0001_initial... OK
      Applying sessions.0001_initial... OK
    ```
    
8. Create admin account
    ```
    (django)$ python manage.py createsuperuser
    Username (leave blank to use 'ubuntu'): admin
    Email address:
    Password:
    Superuser created successfully.
    ```

9. Run server and expose it to the outside
    ```
    (django)$ python manage.py runserver 0.0.0.0:8000
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    January 24, 2020 - 17:35:02
    Django version 3.0.2, using settings 'pollsapi.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CONTROL-C.
    ```
    
10. Access to the server and sign in as an admin. (IP address is hidden for security)
    ```
    https://***.***.***.***:8000/
    ```
    ![image](https://user-images.githubusercontent.com/33472400/74009806-544eee80-49c7-11ea-9b23-a8406bd91a0b.png)

11. Once you have signed in, you can access to the endpoints like:
    ```
    https://***.***.***.***:8000/polls/
    ```
    ![image](https://user-images.githubusercontent.com/33472400/73090831-77d05e80-3f1c-11ea-8fdb-67fb6ab6a485.png)

<br>

How to Test
----------

1. Move to the cloned repository
    ```
    $ cd Django_API
    ```
    
2. Activate the virtual environment
    ```
    $ source django/bin/activate
    ```

3. Move to Django project directory
    ```
    (django)$ cd pollsapi
    ```

4. Run the tests
    ```
    (django)$ python manage.py test
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    ..........
    ----------------------------------------------------------------------
    Ran 14 tests in 5.913s

    OK
    Destroying test database for alias 'default'...
    ```

<br>

Tested Endpoints
----------

- [x] `/polls/`
- [x] `/polls/<pk>/`
- [x] `/polls/<pk>/choices/`
- [x] `/polls/<pk>/choices/<choice_pk>/`
- [x] `/polls/<pk>/choices/<choice_pk/vote/`
- [x] `/login/`
