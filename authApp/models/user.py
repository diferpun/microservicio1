from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """Creates and saves a user with the given username and password."""
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password):

        user = self.create_user(
        username=username,
        password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField('Firstname', max_length = 60)
    lastname = models.CharField('Lastname', max_length = 60)
    username = models.CharField('Username', max_length = 45, unique=True)
    password = models.CharField('Password', max_length = 256)
    email = models.EmailField('Email', max_length = 100)
    isadmi = models.BooleanField(default=True)
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    objects = UserManager()
    USERNAME_FIELD = 'username'