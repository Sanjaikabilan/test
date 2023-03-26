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

class OwnState(models.Model):
    problem = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    domain = models.CharField(max_length=100)

    def __str__(self):
        return self.problem + ' - ' + self.domain

class OwnTeam(models.Model):
    team_name = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(5)])
    leader_name = models.CharField(max_length=50)
    leader_email = models.CharField(max_length=50, unique=True)
    leader_contact = models.CharField(max_length=25, unique=True)
    leader_rollno = models.CharField(max_length=25, unique=True)
    ps = models.ForeignKey(OwnState, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name + ' - ' + self.leader_name

class OwnParticipants(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    contact = models.CharField(max_length=25, unique=True)
    rollno = models.CharField(max_length=25, unique=True)
    team = models.ForeignKey(OwnTeam, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.team.team_name

class Team(models.Model):
    team_name = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(5)])
    leader_name = models.CharField(max_length=50)
    leader_email = models.CharField(max_length=50, unique=True)
    leader_contact = models.CharField(max_length=25, unique=True)
    leader_rollno = models.CharField(max_length=25, unique=True)
    ps = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name + ' - ' + self.leader_name


class Participants(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    contact = models.CharField(max_length=25, unique=True)
    rollno = models.CharField(max_length=25, unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.team.team_name


    













