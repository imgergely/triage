# Generated by Django 4.0.1 on 2022-02-18 17:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('triage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='triage',
            name='Beteg azonosító',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='LF',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='Légzésszám',
        ),
        migrations.RemoveField(
            model_name='triage',
            name='Légút',
        ),
        migrations.AddField(
            model_name='triage',
            name='bor',
            field=models.CharField(choices=[('1', 'Normál'), ('2', 'Meleg'), ('3', 'Hűvös'), ('4', 'Sápadt'), ('5', 'Sárga'), ('6', 'Cyanotikus'), ('7', 'Márványozott'), ('8', 'Kiütéses')], default=1, max_length=1, verbose_name='Bőr'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='kohoges',
            field=models.CharField(choices=[('1', 'Nincs'), ('2', 'Száraz'), ('3', 'Produktív'), ('4', 'Köhécselő'), ('5', 'Rohamszerű'), ('6', 'Inger'), ('7', 'Ugató')], default=1, max_length=1, verbose_name='Köhögés'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='legut',
            field=models.CharField(choices=[('1', 'Átjárható'), ('2', 'Elzáródott'), ('3', 'Stidoros'), ('4', 'Zörgő, szörcsögő'), ('5', 'Sípoló'), ('6', 'Horkoló')], default=1, max_length=1, verbose_name='Légút'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='legzesi_munka',
            field=models.CharField(choices=[('1', 'Normál'), ('2', 'Fokozott'), ('3', 'Gyengülő')], default=1, max_length=1, verbose_name='Légzési munka'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='legzesi_munka_SPO',
            field=models.CharField(default=1, max_length=50, verbose_name='SpO2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='legzesszam',
            field=models.CharField(choices=[('1', 'Normális'), ('2', 'Emelkedett'), ('3', 'Csökkent')], default=1, max_length=1, verbose_name='Légzésszám'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='legzesszam_LF',
            field=models.CharField(default=1, max_length=50, verbose_name='LF'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='patientid',
            field=models.CharField(default=1, max_length=50, verbose_name='Beteg azonosító'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='pulzus',
            field=models.CharField(choices=[('1', 'Ritmusos'), ('2', 'Aritmiás')], default=1, max_length=1, verbose_name='Pulzus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='pulzus_p',
            field=models.CharField(default=1, max_length=50, verbose_name='RR bo'),
            preserve_default=False,
        ),
    ]
