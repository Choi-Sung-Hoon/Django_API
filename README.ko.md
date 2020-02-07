Django_API [![Build Status](https://travis-ci.com/Choi-Sung-Hoon/Django_API.svg?branch=master)](https://travis-ci.com/Choi-Sung-Hoon/Django_API) [![Coverage Status](https://coveralls.io/repos/github/Choi-Sung-Hoon/Django_API/badge.svg?branch=master)](https://coveralls.io/github/Choi-Sung-Hoon/Django_API?branch=master)
==========

CI와 TDD가 적용된 간단한 선거 애플리케이션을 위한 REST API 프로젝트입니다. 이 프로젝트는 Travis CI에 의해서 관리됩니다.

README: [한국어](README.ko.md), [English](README.md)  

<br>

프로젝트 목표
----------

1. **파이썬으로 REST API를 어떻게 디자인하는지** 배우기  
2. **어떻게 좋은 테스트를 만드는지** 배우기  
3. **CI/CD가 어떻게 이루어지는지** 배우기  
4. Django의 구조에 대해서 이해하기  

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

전제 조건
----------

- [virtualenv](https://pypi.org/project/virtualenv/)

<br>

설치
----------

1. 이 레포지토리를 복제하세요
    ```
    $ git clone git@github.com:Choi-Sung-Hoon/Django_API.git
    ```
    
2. 복제된 레포지토리로 이동하세요
    ```
    $ cd Django_API
    ```
    
3. 가상 환경을 생성하세요
    ```
    $ virtualenv django
    Using base prefix '/usr'
    New python executable in /home/ubuntu/Django_API/django/bin/python3.6
    Also creating executable in /home/ubuntu/Django_API/django/bin/python
    Installing setuptools, pip, wheel...
    done.
    ```
    
4. 생성된 가상 환경을 활성화하세요
    ```
    $ source django/bin/activate
    ```
    
5. 필요한 pip 패키지들을 설치하세요
    ```
    (django)$ pip install -r requirements.txt
    ```
    
6. Django 프로젝트 디렉토리로 이동하세요
    ```
    (django)$ cd pollsapi
    ```
    
7. 데이터베이스를 빌드하세요
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
    
8. 어드민 계정을 생성하세요
    ```
    (django)$ python manage.py createsuperuser
    Username (leave blank to use 'ubuntu'): admin
    Email address:
    Password:
    Superuser created successfully.
    ```

9. 서버를 실행하고 외부로 노출시키세요
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
    
10. 브라우저에서 서버에 접속하고 어드민으로 로그인하세요 (IP주소는 보안상 가렸습니다)
    ```
    https://***.***.***.***:8000/
    ```
    ![image](https://user-images.githubusercontent.com/33472400/74009806-544eee80-49c7-11ea-9b23-a8406bd91a0b.png)

11. 한 번 로그인 하고나면, 다음과 같이 endpoint에 접근할 수 있습니다:
    ```
    https://***.***.***.***:8000/polls/
    ```
    ![image](https://user-images.githubusercontent.com/33472400/73090831-77d05e80-3f1c-11ea-8fdb-67fb6ab6a485.png)

<br>

테스트
----------

1. 복제된 레포지토리로 이동하세요
    ```
    $ cd Django_API
    ```
    
2. 가상 환경을 활성화하세요
    ```
    $ source django/bin/activate
    ```

3. Django 프로젝트 디렉토리로 이동하세요
    ```
    (django)$ cd pollsapi
    ```

4. 테스트를 실행하세요
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
