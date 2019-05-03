# Build a blog with Django

First of all make sure System has python3 installed to work with django.

Step-1:
Clone this git link- https://github.com/dhananjayece244/blog.git

Go to blog directory and create a virtual environment using following command- 
$ virtualenv env

then activate the virtual environment- $ source env/bin/activate

Step-2:
Install django: $ pip install django==2.0.7

Step-3:
Run this migtration command - $ python manage.py makemigrations , You will be asked to install some django modules.. so run the following commands before migrations- 

$ pip install django-allauth
$ pip install django-crispy_forms
$ pip install django-tinymce4-lite
$ pip install pillow

step-4: 
Now you can move on and run the migration command-

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

now you can go to admin page(http://127.0.0.1:8000/admin) and can see the database model structure and content.

Thanks---

