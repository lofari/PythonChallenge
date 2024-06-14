from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models


# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    correoElectronico = models.EmailField(max_length=255)


class Vehiculo(models.Model):
    patente = models.CharField(max_length=50, primary_key=True)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="vehiculos")


class Infraccion(models.Model):
    # patente = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name="infraccion")
    patente = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)
    comentarios = models.CharField(max_length=255)


class GenerarInformeRequest(models.Model):
    email = models.EmailField()


class Oficial(AbstractUser):
    nombre = models.CharField(max_length=50)
    uid = models.CharField(max_length=50, unique=True, blank=False)

    USERNAME_FIELD = "uid"
    REQUIRED_FIELDS = ["username"]

