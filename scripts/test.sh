python manage.py migrate rucken_todo 0001_initial
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py test
cd frontend
npm run test