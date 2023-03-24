from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Apply(models.Model):

    problem = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=25)
    

    def __str__(self):
        return self.name + ' - ' + self.problem

class State(models.Model):
    level = (('Easy','Easy'),('Medium','Medium'),('Hard','Hard'))
    doms = (('Energy Engineering','Energy Engineering'),('Electrical and Electronics Engineering','Electrical and Electronics Engineering'),('Textile and Fashion Technology','Textile and Fashion Technology'),('Robotics and Autonomous Systems','Robotics and Autonomous Systems'),)
    contax = (('8754730843','8754730843'), ('9159670084',' 9159670084'), ('7089042384','7089042384'), ('9629013870','9629013870'),)
    cp = (('Janarthanan venkatachalam','Janarthanan venkatachalam'),('Veeramanikandan C','Veeramanikandan C'),('Aditi Nayak','Aditi Nayak'),('Sushrut','Sushrut'),)
    problem = models.CharField(max_length=1000 , blank=True)
    description = models.CharField(max_length=1000, blank=True)
    domain = models.CharField(choices=doms, max_length=100)
    hardness = models.CharField(choices = level,max_length=25)
    contact = models.CharField(choices=contax, max_length=100)
    contact_person = models.CharField(choices=cp, max_length=100,)

    def __str__(self):
        return self.problem + ' - ' + self.domain

class Team (models.Model):
    name = models.CharField( max_length=50 ,validators=[MinLengthValidator(5)])

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=50)
    













