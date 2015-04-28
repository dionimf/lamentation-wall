from django.db import models
import time

from django.core.exceptions import ValidationError

from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractUser, User
from datetime import timedelta
from django.utils import timezone
from django import template

class LamentModel(models.Model):
    text = models.TextField(max_length=300)
    date = models.DateTimeField()
    cries_together = models.IntegerField(default=0)
    user_has_cried = bool

    def save(self):
        if not self.id: # only if it's an insert
            self.date = timezone.now()

        super(LamentModel, self).save()

    def cry(self, user):
        already_cried = LamentCriesModel.objects.filter(user=user.id, lament=self.id)
        print(already_cried)
        if already_cried:
            return -1

        print(2)
        cry = LamentCriesModel()
        cry.lament = self
        cry.user = user
        cry.save()
        print(3)
        
        cry_count = LamentCriesModel.objects.filter(lament=self.id).count()

        return cry_count

    def count_cries(self):
        return LamentCriesModel.objects.filter(lament=self.id).count()

    def calculate_user_cry(self, user):
        if LamentCriesModel.objects.filter(lament=self, user=user):
            self.user_has_cried = True
        else:
            self.user_has_cried = False

    def count_counsels(self):
        return CounselModel.objects.filter(lament_id=self.id).count()

    def uncry(self, user):
        try:
            cry = LamentCriesModel.objects.get(lament=self, user=user)
        except:
            cry = None

        if cry:
            cry.delete()
            
        return self.count_cries()

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

class PostRateModel(models.Model):
    ip = models.GenericIPAddressField()
    date = models.DateTimeField()
    type = models.CharField(max_length=15)

    max_per_minute = 1

    def is_too_much(ip, type):
        time_threshold = timezone.now() - timedelta(minutes=1)

        print(':::' );
        print(time_threshold)

        if (PostRateModel.objects.
            filter(date__gt=time_threshold, type=type, ip=ip).count() >=
            PostRateModel.max_per_minute):

            return True

        return False

class LamentCriesModel(models.Model):
    lament = models.ForeignKey('LamentModel')
    user = models.ForeignKey('UserModel')
    date = models.DateTimeField()

    def save(self):
        if not self.id: # only if it's an insert
            self.date = timezone.now()

        super(LamentCriesModel, self).save()
