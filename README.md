## rucken-todo-django
[![Updates](https://pyup.io/repos/github/rucken/todo-django/shield.svg)](https://pyup.io/repos/github/rucken/todo-django/)
[![Requirements Status](https://requires.io/github/rucken/todo-django/requirements.svg?branch=master)](https://requires.io/github/rucken/todo-django/requirements/?branch=master)
[![Build Status][travis-image]][travis-url]


A simple todo application demonstrating the basic usage of [rucken](https://github.com/rucken) Angular5+ with Django REST framework.


### Usage
- Clone or fork this repository `git clone --recursive https://github.com/rucken/todo-django.git`
- Make sure you have [Python](https://www.python.org/downloads/) installed version 2.7.x
- Make sure you have [node.js](https://nodejs.org/) installed version 6+
- Make sure you have NPM installed version 3+
- Open comand line in folder `todo-django`
- Install virtual env for isolate libs used on project `pip install virtualenv` and init it `virtualenv venv`
- Swicth to virtual env `venv\Scripts\activate` or on windows mingw32 `source venv/Scripts/activate`
- run `pip install -r requirements.txt` to install project dependencies
- run `python manage.py migrate rucken_todo 0001_initial` to init first migrations
- run `python manage.py migrate` to init all migrations
- run `python -c "import shutil; shutil.copy2('README.md', 'frontend/README.md');"` to copy README.md to frontend
- Go to frontend `cd frontend` and run `npm install` to install frontend dependencies
- Build frontend, run `npm run build`
- Collect static `python manage.py collectstatic --noinput`
- Run server `python manage.py runserver 0.0.0.0:5000`
- Open browser to [`http://localhost:5000`](http://localhost:5000)

### Demo application on [Heroku](https://rucken-todo-django.herokuapp.com)
- test admin username: admin, password: 12345678
- test user 1 username: user1, password: 12345678
- test user 2 username: user2, password: 12345678

## License

MIT

[travis-image]: https://travis-ci.org/rucken/todo-django.svg?branch=master
[travis-url]: https://travis-ci.org/rucken/todo-django
