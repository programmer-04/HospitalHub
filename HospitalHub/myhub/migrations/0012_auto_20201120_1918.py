# Generated by Django 3.1.3 on 2020-11-20 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhub', '0011_auto_20201112_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile',
            field=models.ImageField(default='default.jpg', upload_to='media'),
        ),
    ]