cp .env.prod .env
gunicorn ufanutom.wsgi:application --workers 4