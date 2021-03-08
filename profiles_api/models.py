from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def  create_user(self, email, name, password=None):
        """create new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        email=self.normalize_email(email)
        user=self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create new superuser"""
        user=self.create_user(email, name, password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIERD_FIELDS=['name',]

    def get_fullname(self):
        """retrieve full name"""
        return self.name

    def get_shortname(self):
        """retrieve short name"""
        return self.name

    def __str__(self):
        return self.email
