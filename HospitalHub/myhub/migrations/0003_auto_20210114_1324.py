# Generated by Django 3.1.1 on 2021-01-14 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhub', '0002_auto_20210113_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_review',
            name='comment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='hospital_review',
            name='comment',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
