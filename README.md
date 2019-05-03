# Build a blog with Django

System should have python3 installed because django follows python language.

Step-1:
Clone this git link- 
Go to your working blog directory and a virtual environment using following command- 
$ virtualenv env

Activate virtual environment- $source env/bin/activate

Step-2:
Install django: pip install django==2.0.7

Step-3:
Run this migtration command - $ python manage.py makemigrations , You will be asked install some django modules so run the following command before migrations- 
$ pip install django-allauth
$ pip install django-crispy_forms
$ pip install django-tinymce4-lite
$ pip install pillow

step-4: 
Now you are can move on and run migration command-

$ python manage.py makemigrations
$ python manage.py migrate

step-4:

Now you can start server-
$ python manage.py runserver

Open this localhost address in your brawser- http://127.0.0.1:8000/

--------------------------------------------------------------------------------------

Now create a super user so that you can access admin page and create blog post and polls.

$ python manage.py createsuperuser
Set a username and password 

then move to admin page(http://127.0.0.1:8000/admin) and now you can see the database structure.

Thanks---

