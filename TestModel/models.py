from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)

class Task(models.Model):
    tnum = models.CharField(max_length=20)
    tjob = models.CharField(max_length=20)
    tgit = models.CharField(max_length=20)
class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    note = models.CharField(max_length=32)
class Democtl(models.Model):
    demoname = models.CharField(max_length=32)
    demoattr = models.CharField(max_length=16)
    demohost = models.CharField(max_length=32)
    demoport = models.CharField(max_length=32)
    demostate = models.CharField(max_length=16)
    democmdname = models.CharField(max_length=32)
class Demostate(models.Model):
    demoname = models.CharField(max_length=32)
    demoattr = models.CharField(max_length=16)
    demohost = models.CharField(max_length=32)
    demoport = models.CharField(max_length=32)
    demostate = models.CharField(max_length=16)
