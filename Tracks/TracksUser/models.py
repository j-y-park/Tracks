from django.db import models

# Create your models here.

class TracksUser(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    USERNAME_FIELD = 'email'
