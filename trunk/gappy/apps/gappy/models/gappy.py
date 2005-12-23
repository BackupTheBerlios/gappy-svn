from django.core import meta
from django.models.auth import User

# Understand that a user can represent one of two things:
# 1) A group of students.
# 2) A single person acting as an administrator.
#
# This is why users only belong to one class.
class Course(meta.Model):
    cname = meta.TextField(maxlength=100)

class GappyUser(meta.Model):
    class META:
        permissions = (
            ("can_set_appointment", "Can create or delete appointment times"),
            ("can_choose_appointment", "Can choose an appointment time"),
            )
    user = meta.OneToOneField(User)
    course = meta.ForeignKey(Course)

class Project(meta.Model):
    pname = meta.TextField(maxlength=100)
    course = meta.ForeignKey(Course)

class DemoTime(meta.Model):
    time = meta.DateTimeField()
    demoer = meta.ForeignKey(GappyUser)
    demoee = meta.ForeignKey(GappyUser)
    course = meta.ForeignKey(Course)
