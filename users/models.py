from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    tg_id = models.BigIntegerField(verbose_name=_('telegram ID'))

    REQUIRED_FIELDS = []
