#!/bin/sh
echo "Waiting Postgres to start..."
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
  sleep 0.1
done

echo "Postgres started, setting up database"

# Creating database if not exists
python bin/createdb.py

# Running database migrations
python manage.py migrate

# Run database seeds
python manage.py adminuser --username $ADMIN_LOGIN --password $ADMIN_PASSWORD --noinput --email $ADMIN_EMAIL --preserve

# Run crowdsale stages seeds
python manage.py shell < bin/create_settings_seeds.py

