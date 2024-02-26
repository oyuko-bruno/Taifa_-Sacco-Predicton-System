# authentication/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields you need
    first_name = models.CharField(max_length=30, blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Last Name')
    id_number = models.CharField(max_length=15, blank=True, verbose_name='ID Number')

    # Add related_name to avoid clashes with reverse accessor for groups
   # groups = models.ManyToManyField(
      #  'auth.Group',
      #  related_name='customuser_set',
       # blank=True,
       # verbose_name='groups',
       # help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
   # )

    # Add related_name to avoid clashes with reverse accessor for user_permissions
   # user_permissions = models.ManyToManyField(
      #  'auth.Permission',
     #   related_name='customuser_set',
      #  blank=True,
      #  verbose_name='user permissions',
      #  help_text='Specific permissions for this user.',
    #)
    #Username:Brunoadmin
    #pass:12345678
