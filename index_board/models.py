from django.db import models
import time

from django.core.exceptions import ValidationError

from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractUser, User


class LamentModel(models.Model):
    text = models.TextField(max_length=300)
    date = models.DateTimeField(default=None)
    cries_together = models.IntegerField(default=0)

    def save(self):
        self.date = time.strftime('%Y-%m-%d %H:%M:%S')
        super(LamentModel, self).save()

    def count_counsels(self):
        return CounselModel.objects.filter(lament_id=self.id).count()

class CounselModel(models.Model):
    lament_id = models.ForeignKey('LamentModel')
    text = models.TextField()
    test = models.TextField()

class VisitModel(models.Model):
    ip = models.GenericIPAddressField()
    date = models.DateTimeField()
    request_method = models.CharField(max_length=10)

class UserModel(AbstractUser):
    pass
