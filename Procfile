release: python manage.py migrate
web: gunicorn tigerears2.wsgi --timeout 60 --log-file -