from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4 , unique=True ,primary_key=True,editable=False)
    is_admin= models.BooleanField('Is admin', default=False)
    is_member = models.BooleanField('Is member', default=False)

class UserExpenses(models.Model):
    Category=(('Health','Health'),
    ('Electronics','Electronics'),
    (' Travel',' Travel'),
    ('Education','Education'),
    ('Books','Books'),
    ('Others','Others'))
    
    owner=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE,related_name='expenses')
    Name=models.CharField(max_length=20)
    Date_of_Expense=models.DateTimeField(auto_now_add=False)
    Category=models.CharField(max_length=200,choices=Category)
    Description=models.TextField(null=True,blank=True)
    Amount=models.FloatField(default=0,null=True,blank=True)
    Created=models.DateTimeField(default=timezone.now, editable=False, blank=True)
    Updated=models.DateTimeField(auto_now_add=True)
