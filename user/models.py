
from django.db import models

from django.contrib.auth.models import AbstractBaseUser

### manager imports

from user.model_managers import USER_MANAGER

### other imports

from uuid import uuid4

from user.utils import validate_pincode

# Create your models here.

class User(AbstractBaseUser):
    id = models.UUIDField(
        verbose_name='user id',
        primary_key=True,
        default=uuid4,
    )

    email = models.EmailField(
        unique=True,
        max_length=126,
    )

    name = models.CharField(
        max_length=126,
    )

    phone = models.CharField(
        max_length=10,
        unique=True,
    )

    address = models.CharField(
        max_length=500,
    )

    pincode = models.CharField(
        max_length=6,
        validators = [validate_pincode],
    )

    is_verified_email = models.BooleanField(default=False)

    is_verified_phone = models.BooleanField(default=False)

    object = USER_MANAGER()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'id'

    REQUIRED_FIELDS = ['email','name','phone']

    class _Meta:
        model_label='user'

    def verified_email(self):
        self.is_verified_email = True
        self.save()

    def veified_phone(self):
        self.is_verified_phone = True
        self.save()

class Backet(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
    )

    user_id = models.UUIDField(
        verbose_name='user id for backet',
        blank=False,
        null = False,
    )

    products_id = models.JSONField(
        verbose_name='product list',
        blank=True,
        null=True,
    )

    class _Meta:
        model_label = 'user_backet'
