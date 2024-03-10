from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator
from datetime import date

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Add a field to track when the record was last updated
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=150, unique=True)  # Ensure email is unique across records
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, default=None)  # Add a ForeignKey field to associate each record with a user

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_address(self):
        return f"{self.address}, {self.city}, {self.state} {self.zipcode}"


class Appointment(models.Model):
    SELLING_OPTIONS = [
        ('sell', 'Sell'),
        ('donate', 'Donate'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=15, validators=[MinLengthValidator(10), RegexValidator(r'^[0-9]*$', message='Phone number must contain only digits.')])
    address = models.CharField(max_length=100)
    calendar = models.DateField(default=date.today)  # Use date.today() for the default value
    Created_By = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)    
    selected_person = models.ForeignKey(Record, on_delete=models.SET_NULL, null=True, blank=True)
    selling_option = models.CharField(max_length=10, choices=SELLING_OPTIONS, null=True, blank=True)

    def __str__(self):
        return f"{self.full_name}"



class Compost_inquiry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Created_By = models.ForeignKey(User,on_delete=models.CASCADE,null=True, default =None)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
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