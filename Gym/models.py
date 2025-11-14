from datetime import datetime, timedelta

from django.db import models

# Create your models here

class Trainers(models.Model):
    full_name = models.CharField(max_length=100, null=False, blank=False)
    joined_date = models.DateField(auto_now_add=True)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - ACTIVE: {self.active}"

# GYM CLIENT
class ClientGym(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    surname = models.CharField(max_length=100, null=False, blank=False)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    cc = models.BigIntegerField(unique=True)
    payed = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)
    check_in = models.TimeField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"
    
    # RETURN DAYS AVAILABLES 
    def days_available(self):
        if self.payed:
            return abs((self.finish_date - datetime.today().date()).days)

        else:
            return 0
    
    # METHOD FOR RESTART DATES OF CLIENT
    def restart_dates(self):
        self.start_date = datetime.today().date()
        self.finish_date = self.start_date + timedelta(days=31) 

    

