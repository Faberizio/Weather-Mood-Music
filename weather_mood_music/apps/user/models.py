from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext as _

class User(AbstractUser):
    title = models.CharField(max_length=100, null=True, help_text='Your profession')
    birthday = models.DateField(null=True, blank=True)

    class Meta:
        ...
        
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_set'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_set_permissions'
    )
