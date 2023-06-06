from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class usr(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email
    

class Profile(models.Model):

#    Description 
    description = models.CharField(max_length=1000, null=True)
    photo = models.ImageField(null=True)

#    Basic Details
    profile_for = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=256, null=True)
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    body_type = models.CharField(max_length=20, null=True)
    physical_status = models.CharField(max_length=30, null=True)
    martial_status = models.CharField(max_length=50, null=True)
    mother_tongue = models.CharField(max_length=50, null=True)
    drinking_habits = models.CharField(max_length=30, null=True)
    smoking_habits = models.CharField(max_length=50, null=True)
    eating_habits = models.CharField(max_length=50, null=True)


# Religion
    religion = models.CharField(max_length=100, null=True)
    caste = models.CharField(max_length=100, null=True)
    sub_caste = models.CharField(max_length=100, null=True)
    gothram = models.CharField(max_length=50, null=True)
    zodiac_sign = models.CharField(max_length=30, null=True)
    star = models.CharField(max_length=50,null=True)
    dosham = models.CharField(max_length=50, null=True)
    time_of_birth = models.TimeField(auto_now=False, auto_now_add=False)
    place_of_birth = models.TimeField(auto_now=False, auto_now_add=False)

     
# User Location
    country = models.CharField(max_length=30 , null=True)
    state = models.CharField(max_length=30 , null=True)
    city = models.CharField(max_length=30 , null=True)
    citizenship = models.CharField(max_length=30, null=True)
    native = models.CharField(max_length=30, null=True)

# Professional Information
    education = models.CharField(max_length=100, null=True)
    education_in_detail =models.CharField(max_length=100, null=True)
    college = models.CharField(max_length=100, null=True)
    occupation = models.CharField(max_length=100, null=True)
    occupation_desc = models.CharField(max_length=100, null=True)
    organization = models.CharField(max_length=100, null=True)
    annual_income = models.CharField(max_length=100, null=True)

# Family details
    family_values = models.CharField(max_length=50,null=True)
    family_type = models.CharField(max_length=20 ,null=True)
    family_status = models.CharField(max_length=100, null=True)
    father_occupation = models.CharField(max_length=100, null=True)
    mother_occupation = models.CharField(max_length=100, null=True)
    no_of_brothers = models.IntegerField(default=0)
    no_of_sisters = models.IntegerField(default=0)
    family_location = models.CharField(max_length=100, null=True)
    phone_number = models.BigIntegerField(null=True)


# About Family
    family_desc = models.CharField(max_length=1000)


# Hobbies and Intrests
    hobbies = models.CharField(max_length=256)
    