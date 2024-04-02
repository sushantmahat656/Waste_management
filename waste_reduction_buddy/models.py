from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from datetime import date
from datetime import datetime

class Record(AbstractUser):
    full_name = models.CharField(max_length=100, default=None)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,null=True)    
    nin = models.CharField(max_length=20)

    # Specify custom related names for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='record_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='record_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    # Make username nullable
    username = models.CharField(max_length=150, unique=True, null=True)
    password = models.CharField(max_length=128, default='')

    def __str__(self):
        return self.full_name


class Appointment(models.Model):
    SELLING_OPTIONS = [
        ('SELL', 'Sell'),
        ('DONATE', 'Donate'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, validators=[MinLengthValidator(10), RegexValidator(r'^[0-9]*$', message='Phone number must contain only digits.')])
    address = models.CharField(max_length=100)
    calendar = models.DateField(default=date.today)
    appointment_time = models.TimeField(default=datetime.now().time())  
    Created_By = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)    
    selected_person = models.ForeignKey(Record, on_delete=models.SET_NULL, null=True, blank=True)
    selling_option = models.CharField(max_length=10, choices=SELLING_OPTIONS, null=True, blank=True)

    def __str__(self):
        return f"{self.full_name}"



class Compost_inquiry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Created_By = models.ForeignKey(User,on_delete=models.CASCADE,null=True, default =None)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    quantity = models.IntegerField()
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.full_name


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact_Us(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Created_By = models.ForeignKey(User,on_delete=models.CASCADE,null=True, default =None)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name