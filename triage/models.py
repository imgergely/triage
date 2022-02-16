from django.db import models
from django.conf import settings


LEGUT_CHOICES = (
        ('1', 'Átjárható',),
        ('2', 'Elzáródott',),
        ('3', 'Stidoros',),
        ('4', 'Zörgő, szörcsögő',),
        ('5', 'Sípoló',),
        ('6', 'Horkoló',),
    )

LEGZESSZAM_CHOICES = (
        ('1', 'Normális',),
        ('2', 'Emelkedett',),
        ('3', 'Csökkent',),
    )

LEGZESI_MUNKA_CHOICES = (
        ('1', 'Normál',),
        ('2', 'Fokozott',),
        ('3', 'Gyengülő',),
    )

KOHOGES = (
        ('1', 'Nincs',),
        ('2', 'Száraz',),
        ('3', 'Produktív',),
        ('4', 'Köhécselő',),
        ('5', 'Rohamszerű',),
        ('6', 'Inger',),
        ('7', 'Ugató',),
    )

class Triage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    patientid = models.CharField(max_length=50, name="Beteg azonosító")
    legut = models.CharField(max_length=1,choices=LEGUT_CHOICES,name="Légút")    
    legzesszam = models.CharField(max_length=1,choices=LEGZESSZAM_CHOICES,name="Légzésszám")
    legzesszam_LF = models.CharField(max_length=50, name="LF")
    legzesi_munka = models.CharField(max_length=1,choices=LEGZESI_MUNKA_CHOICES,name="Légzési munka")
    legzesi_munka_SPO = models.CharField(max_length=50, name="SpO2")
    kohoges = models.CharField(max_length=1,choices=KOHOGES,name="Köhögés")

    def __str__(self):
        return self.patientid
