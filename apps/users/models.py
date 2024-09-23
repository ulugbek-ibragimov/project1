from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.managers import UserManager
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    first_name = None
    last_name = None
    email = None
    login = models.CharField(
        _('Login'),
        max_length=100,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ))
    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = []
    objects = UserManager()
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Add a custom related_name here
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Add a custom related_name here
        blank=True,
        help_text='Specific permissions for this user.'
    )