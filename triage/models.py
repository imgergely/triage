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

LEGZESSZAM = (
        ('1', 'Normális',),
        ('2', 'Emelkedett',),
        ('3', 'Csökkent',),
    )

LEGZESI_MUNKA = (
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

KOHOGES = (
        ('1', 'Nincs',),
        ('2', 'Száraz',),
        ('3', 'Produktív',),
        ('4', 'Köhécselő',),
        ('5', 'Rohamszerű',),
        ('6', 'Inger',),
        ('7', 'Ugató',),
    )

PULZUS = (
        ('1', 'Ritmusos',),
        ('2', 'Aritmiás',),
    )

BOR = (
        ('1', 'Normál',),
        ('2', 'Meleg',),
        ('3', 'Hűvös',),
        ('4', 'Sápadt',),
        ('5', 'Sárga',),
        ('6', 'Cyanotikus',),
        ('7', 'Márványozott',),
        ('8', 'Kiütéses',),
    )

class Triage(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    patientid = models.CharField(max_length=50, name="Beteg azonosító")
    legut = models.CharField(max_length=1,choices=LEGUT_CHOICES,name="Légút")    
    legzesszam = models.CharField(max_length=1,choices=LEGZESSZAM,name="Légzésszám")
    legzesszam_LF = models.CharField(max_length=50, name="LF")
    legzesi_munka = models.CharField(max_length=1,choices=LEGZESI_MUNKA,name="Légzési munka")
    legzesi_munka_SPO = models.CharField(max_length=50, name="SpO2")
    kohoges = models.CharField(max_length=1,choices=KOHOGES,name="Köhögés")
    pulzus = models.CharField(max_length=1,choices=PULZUS,name="Pulzus")
    pulzus_p = models.CharField(max_length=50, name="P")
    bor = models.CharField(max_length=1,choices=BOR,name="Bőr")
    pulzus_p = models.CharField(max_length=50, name="CRT")
    pulzus_p = models.CharField(max_length=50, name="RR bo")

    def __str__(self):
        return self.patientid

