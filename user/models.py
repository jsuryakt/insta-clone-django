from django.db import models
from django.contrib.auth.models import AbstractUser
from user.manager import CustomUserManager
# Create your models here.
# class User(AbstractUser):
#     picture = models.ImageField(upload_to='profile_pictures')

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []

#     # objects = AbstractUserManager()

#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user


class User(AbstractUser):
    picture = models.ImageField(
        upload_to='profile_pictures', null=False, blank=False)
    full_name = models.CharField(max_length=100, default="Fullname not set")
    email = models.EmailField(unique=True)

    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email