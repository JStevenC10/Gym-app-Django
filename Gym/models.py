from django.db import models

# Create your models here.

# GYM CLIENT
class ClientGym(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    surname = models.CharField(max_length=100, null=False, blank=False)
    nickname = models.CharField(max_length=100, null=True, blank=True)
    cc = models.BigIntegerField()
    payed = models.BooleanField(default=False)
    start_date = models.DateField()
    finish_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

