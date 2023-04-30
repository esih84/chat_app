from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError('please enter an email')

        if not username:
            raise ValueError('please enter an username')

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
       user = self.create_user(email, username, password)
       user.is_admin = True
       user.save(using=self._db)
       return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    user_id = models.AutoField(primary_key=True, auto_created=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

