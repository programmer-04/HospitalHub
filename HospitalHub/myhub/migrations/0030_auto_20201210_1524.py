# Generated by Django 3.1.3 on 2020-12-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhub', '0029_auto_20201124_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='building',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='street',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
