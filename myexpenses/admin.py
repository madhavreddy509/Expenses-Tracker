from django.contrib import admin
from . models import User,UserExpenses
# Register your models here.
admin.site.register(User)
admin.site.register(UserExpenses)
