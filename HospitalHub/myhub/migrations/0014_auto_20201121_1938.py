# Generated by Django 3.1.3 on 2020-11-21 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhub', '0013_ambulance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='profile',
        ),
        migrations.DeleteModel(
            name='ambulance',
        ),
    ]