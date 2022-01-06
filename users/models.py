from django.db import models
from django.contrib.auth.models import  AbstractUser
# Create your models here.
class Subscription(models.Model):
    TYPE=[
    ('Basic','Basic'),
    ('Standard','Standard'),
    ('Premium','Premium'),
    ]
    subscription_type = models.CharField(choices=TYPE,max_length=255)
    subscription_amount=models.IntegerField(null=True,blank=True)
    CHOICE=(
    ('M','Monthly'),
    ('Y','Yearly'),
    )
    time_validity_option=models.CharField(choices=CHOICE,max_length=255)
    time_validity=models.IntegerField(null=True,blank=True)    
    def __str__(self):
        return f"{self.subscription_type}"
    
class SchoolUser(AbstractUser):
    name=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(max_length=255,verbose_name="Email",null=True,blank=True)
    phone_no=models.IntegerField(verbose_name="Phone Number",null=True,blank=True)
    username=models.CharField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    subscription_id=models.ForeignKey(Subscription,on_delete=models.CASCADE)
    password=models.CharField(max_length=255,null=True,blank=True)
    
    NAME="name"
    EMAIL_FIELD="email"
    PHONE_NO="phone_no"
    USERNAME_FIELD="username"
    IS_ACTIVE="is_active" 
    SUBSCRIPTION_ID="subscription_id"
    PASSWORD="password"
    
    
