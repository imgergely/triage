from django.db import models
from django.conf import settings
from operator import methodcaller


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

TRIAGE_CATEGORY = (
        ('1', '1 - Azonnali - P',),
        ('2', '2 - 15 perc - S',),
        ('3', '3 - 30 perc - Z',),
        ('4', '4 - 60 perc - K',),
        ('5', '5 - 120 perc - Sz',),
    )

class Triage(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True) #user model field is used to represent the person treating the patient
    patientid = models.CharField("Beteg azonosító", max_length=50, unique=True)
    legut = models.CharField("Légút",max_length=1,choices=LEGUT_CHOICES)    
    legzesszam = models.CharField("Légzésszám", max_length=1,choices=LEGZESSZAM)
    legzesszam_LF = models.CharField("LF",max_length=50)
    legzesi_munka = models.CharField("Légzési munka",max_length=1,choices=LEGZESI_MUNKA)
    legzesi_munka_SPO = models.CharField("SpO2",max_length=50)
    kohoges = models.CharField("Köhögés",max_length=1,choices=KOHOGES)
    pulzus = models.CharField("Pulzus",max_length=1,choices=PULZUS)
    pulzus_p = models.CharField("P",max_length=50)
    bor = models.CharField("Bőr",max_length=1,choices=BOR)
    crt = models.CharField("CRT",max_length=50) 
    rrbo = models.CharField("RR bo",max_length=50)
    treatment = models.BooleanField("Kezelés alatt", default=False)
    triage_category = models.CharField("Triage Kategória",max_length=1,choices=TRIAGE_CATEGORY)

    def get_fields(self):
        collectorlist = []
        for field in Triage._meta.fields:
            if field.name not in ['id', 'created','user']:
                try:
                    collector = field.verbose_name, methodcaller('get_{}_display'.format(field.name))(self)
                    collectorlist.append(collector)
                except:
                    collector= field.verbose_name, field.value_to_string(self)
                    collectorlist.append(collector)
        return collectorlist
