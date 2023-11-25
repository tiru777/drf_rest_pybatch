from django.contrib import admin
from app.models import Employee

class MyEmployee(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')


admin.site.register(Employee, MyEmployee)