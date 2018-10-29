from django.db import models
from django.utils import timezone

# Create your models here.


class BankModel(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    entered_date = models.DateTimeField(default=timezone.now)


# class AccountModel(models.Model):
#
#
# class Transactions(models.Model):



def publish(self):
    self.entered_date = timezone.now()
    self.save()


def __str__(self):
    return self.username
