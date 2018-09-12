StuffZilla
==========

Gobal merry-go-round for stuff that is waiting to be used, shared and enjoyed by friends.

  <a href="https://github.com/vchaptsev/cookiecutter-django-vue">
      <img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg" />
  </a>

  ## Apps
  - config
  - feedback
  - market
  - position
  - stuffzilla: Main
  - userprofile: Extension for User

  ## License
  MIT

  ## BUILD WITH:
  Django Vue Cookiecutter
  https://github.com/vchaptsev/cookiecutter-django-vue  

  ## Docker
  https://docs.docker.com/

  sudo docker-compose run django python manage.py <command>

  User issue (Permission):
  sudo docker-compose run --user=root django python manage.py <command>

  ## Reset Db
  sudo docker-compose run --user=root django python manage.py reset_db
  sudo docker-compose run --user=root django python manage.py makemigrations
  sudo docker-compose run --user=root django python manage.py migrate
  sudo docker-compose run --user=root django python manage.py createsuperuser

  ## Media (static) Issues
  The folder media/ and static/ need to be accessible by the django user.
  sudo docker-compose run --user=root django chown 1000:django media -R
  sudo docker-compose run --user=root django chown 1000:django stuffzilla/static -R

  ## New Django App: xyz
  sudo docker-compose run --user=root django python manage.py startapp xyz
  sudo docker-compose run --user=root django chown 1000:django xyz -R
