from django.db import models
from django.contrib.auth.models import AbstractUser

# 2 . After clicking the signup , it will go to register page there the user has to enter 
# Name , Email , Phone Number , Password , Confirm Password but after entering the email id 
# a OTP will be sended to that mailid and it should be verified then after clicking the register button , 
# the user will be registered.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    otp = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
