# Install external

## Install GIT
https://git-scm.com/download/win
## Install SourceTree
https://www.sourcetreeapp.com/
## Install Visual Studio Code
https://code.visualstudio.com/

# Prepare backend

## Install external

### Install Python 2.7
http://docs.python-guide.org/en/latest/starting/install/win/
### Install Heroku CLI
https://devcenter.heroku.com/articles/heroku-command-line

## Install
```
pip install virtualenv
virtualenv venv
source venv/Scripts/activate
#venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
pip freeze > requirements.txt
python manage.py createsuperuser
```
## Start server
```
source venv/Scripts/activate
#venv\Scripts\activate
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
#admin: pa55w0rd
python manage.py makemigrations -n Name
python manage.py makemigrations --empty rucken_todo -n Name
python manage.py runserver 0.0.0.0:5000
```
## Push repository
```
git add .
git commit -m "prepare backend"
git push -u origin master
```
# Prepare frontend

## Install external

### Install NodeJS 6
https://nodejs.org/en/

## Install
```
npm install -g npm
npm install -g angular-cli
npm install -g typings
cd frontend
npm install
```
## Run standalone frontend application with watch
```
cd frontend
ng serve --env=dev
```
## Run frontend application from backend 

### Build and copy frontend files to backend
```
cd frontend
ng build --env=prod
```
### Run backend server
```
source venv/Scripts/activate
python manage.py migrate rucken_todo 0001_initial
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:5000
```
## Push repository
```
git add .
git commit -m "deploy"
git push -u origin master
```