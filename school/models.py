from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=25)


class Log(models.Model):
    request_path = models.CharField(max_length=50)
    request_method = models.CharField(max_length=50)
    execution_time = models.CharField(max_length=50)
