# Generated by Django 4.0.2 on 2022-03-02 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triage', '0003_triage_crt_triage_rrbo_alter_triage_patientid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='triage',
            name='treatment',
            field=models.BooleanField(default=False, verbose_name='Beteg Státusz'),
        ),
    ]
