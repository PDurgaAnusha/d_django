from django.db import models
from django.contrib.auth.models import User # imports user data models from django authentications.the user table in the database it is a built in model


class TODOO(models.Model):
    srno=models.AutoField(auto_created=True,primary_key=True)
    title= models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False,blank=True,)
    user = models.ForeignKey( User, on_delete=models.CASCADE)





# django-admin startproject tododjango ---to strat project
#py manage.py makemigrations tododjango ---to make migrations
#  py manage.py migrate                
# Operations to perform: Apply all migrations: admin, auth, contenttypes, sessions, tododjango
#  py manage.py createsuperuser    ---create user with credentinals
# py manage.py runserver    


# localhost/admin ----enter the user details