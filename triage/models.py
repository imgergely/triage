from django.db import models
from django.conf import settings

class TriageA(models.Model):
    LEGUT_CHOICES = (
        ('1', 'Átjárható',),
        ('2', 'Elzáródott',),
        ('3', 'Stidoros',),
        ('4', 'Zörgő, szörcsögő',),
        ('5', 'Sípoló',),
        ('6', 'Horkoló',),
    )
    legut = models.CharField(
        max_length=1,
        choices=LEGUT_CHOICES,
        name="Légút"
    )

class TriageB(models.Model):   
    LEGZESSZAM_CHOICES = (
        ('1', 'Normális',),
        ('2', 'Emelkedett',),
        ('3', 'Csökkent',),
    )
    legzesszam = models.CharField(
        max_length=1,
        choices=LEGZESSZAM_CHOICES,
        name="Légzésszám"
    )
    legzesszam_LF = models.CharField(max_length=50, name="LF")

