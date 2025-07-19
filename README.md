# CRUD_DjangoRestFramework

After Installing all the requirements like pip install django pip install djangorestframework

Create a new Django project and app

django-admin startproject api
cd api
django-admin startapp myapp

Add rest_framework and your app to the INSTALLED_APPS in settings.py

Define your models in myapp/models.py

Run the migrations to create the database tables
python manage.py makemigrations
python manage.py migrate

Create a serializer for your model in myapp/serializers.py

Create views to handle API requests in myapp/views.py

Define the URL patterns for your API in myapp/urls.py and also define in your project main urls.py

Start the Django development server
python manage.py runserver
