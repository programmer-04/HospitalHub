# Generated by Django 3.1.2 on 2020-11-24 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhub', '0028_hospital_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='city',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
