release: python manage.py migrate
web: gunicorn tigerears2.wsgi --log-file --timeout 60 -