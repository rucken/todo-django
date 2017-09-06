python manage.py migrate
python manage.py collectstatic --noinput
python manage.py test
cd frontend
npm run test