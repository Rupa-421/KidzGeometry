web: gunicorn kidzgeometry.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
opencv-python-headless==4.2.0.32