from django.core import meta

# Create your models here.
class User(meta.Model):
    username = meta.CharField(maxlength=20)
    passwd = meta.CharField(maxlength=20)
    real_name = meta.TextField(maxlength=50)
    superuser = meta.BooleanField()

class Course(meta.Model):
    cid = meta.IntegerField()
    cname = meta.TextField(maxlength=100)

class Project(meta.Model):
    pid = meta.IntegerField()
    pname = meta.TextField(maxlength=100)

class DemoTime(meta.Model):
    time = meta.DateTimeField()
