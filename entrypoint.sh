#!/bin/sh

echo 'Waiting for mysql...'

while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
    sleep 0.1
done

echo 'mysql started 🎉'

echo 'Running migrations...'
python manage.py migrate

echo 'Collecting static files...'
python manage.py collectstatic --no-input

exec "$@"