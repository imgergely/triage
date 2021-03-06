# Generated by Django 4.0.1 on 2022-02-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triage', '0002_remove_triage_beteg azonosító_remove_triage_lf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='triage',
            name='crt',
            field=models.CharField(default=1, max_length=50, verbose_name='CRT'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triage',
            name='rrbo',
            field=models.CharField(default=1, max_length=50, verbose_name='RR bo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='triage',
            name='patientid',
            field=models.CharField(max_length=50, unique=True, verbose_name='Beteg azonosító'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='pulzus_p',
            field=models.CharField(max_length=50, verbose_name='P'),
        ),
    ]
