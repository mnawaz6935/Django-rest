from django.db import models


# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_ref = models.TextField(unique=True)
    product_title = models.TextField()
    product_slug = models.TextField()
    product_category = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.TextField()
    last_name = models.TextField()
    education = models.TextField()
    city = models.TextField()
    contact = models.TextField()
    ppsc_attempts = models.TextField()
    gender = models.TextField()
    purpose = models.TextField()
    category = models.TextField()
    device_id = models.TextField()
    device_name = models.TextField()
    signup_date = models.DateTimeField(auto_now=True)
    membership_start_date = models.DateTimeField(auto_now=True)
    membership_end_date = models.DateTimeField(auto_now=True)
    device_login_date = models.DateTimeField(auto_now=True)
