from django.contrib import admin

# Register your models here.
from  .models import Record,Appointment

admin.site.register(Record)
admin.site.register(Appointment)
