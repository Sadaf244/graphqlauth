from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.
class SchoolUser(AbstractUser):
    name=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(max_length=255,verbose_name="Email",null=True,blank=True)
    phone_no=models.IntegerField(verbose_name="Phone Number",null=True,blank=True)
    username=models.CharField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    password=models.CharField(max_length=255,null=True,blank=True)
    
    NAME="name"
    EMAIL_FIELD="email"
    PHONE_NO="phone_no"
    USERNAME_FIELD="username"
    IS_ACTIVE="is_active" 
    PASSWORD="password"
    
    