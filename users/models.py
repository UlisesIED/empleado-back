from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from uuid import uuid4

class Persona(models.Model):
    nombre = models.CharField(max_length=32, null=False)
    a_paterno = models.CharField(max_length=32, null=False)
    a_materno = models.CharField(
        max_length=32, 
        null=True, 
        blank=True
    )
    class Meta:
        abstract = True
        

class UserManager(BaseUserManager):
    def create_user(self, username, role= None, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username,  role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, role = None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, role, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    
    ADMIN = 1
    EMPLOYEE = 2
    
    
    ROL_CHOICES = (
        (ADMIN,'Administrador'),
        (EMPLOYEE,'Empleado')
    )
    
    
    id = models.UUIDField(default=uuid4, unique=True, editable=False, primary_key=True)
    username = models.CharField(max_length=64, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role=models.PositiveSmallIntegerField(choices=ROL_CHOICES, blank=True, null=True)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role']    
