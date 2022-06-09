from django.db import models
from django.forms import EmailField

# Create your models here

class people(models.Model):
    username = models.CharField(max_length=150)
    firstname = models.CharField(max_length=10000)
    lastname = models.CharField(max_length=10000)
    email = models.EmailField()
    nationality = models.CharField(max_length=10000)
    state = models.CharField(max_length=10000)
    gender = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class address(models.Model):
    user_address = models.CharField(max_length=10000)
    state = models.CharField(max_length=10000)
    city = models.CharField(max_length=10000)
    postcode = models.CharField(max_length=10000)
    user = models.ForeignKey(people, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_address


class product(models.Model):
    p_name = models.CharField(max_length=10000)
    p_price = models.CharField(max_length=10000)
    p_color = models.CharField(max_length=10000)
    p_brand = models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.p_name


class doctor(models.Model):
    fullname = models.CharField(max_length=10000)
    hospital_name = models.CharField(max_length=10000, null=True)
    hospital_location = models.CharField(max_length=10000, null=True)
    specialization = models.CharField(max_length=10000)
    experience = models.CharField(max_length=10000)
    gender = models.CharField(max_length=10000)
    email = models.EmailField()
    patient = models.ManyToManyField(people)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname



class profile(models.Model):
    bio = models.CharField(max_length=10000)
    username = models.OneToOneField(people, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bio

    

